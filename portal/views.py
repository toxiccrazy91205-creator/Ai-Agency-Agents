import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from openai import OpenAI
from .utils import get_all_agents, get_agent_by_id
from .models import ChatMessage

def index(request):
    """
    Renders the agent dashboard.
    """
    agents_by_category = get_all_agents()
    return render(request, 'portal/index.html', {
        'agents_by_category': agents_by_category
    })

def agent_chat(request, category, agent_id):
    """
    Renders the chat interface for a specific agent with history.
    """
    agent = get_agent_by_id(category, agent_id)
    if not agent:
        return redirect('index')
    
    # Load separate chat history for this agent
    history = ChatMessage.objects.filter(category=category, agent_id=agent_id).order_by('timestamp')
    
    return render(request, 'portal/chat.html', {
        'agent': agent,
        'history': history
    })

@csrf_exempt
def chat_api(request):
    """
    API endpoint for handling chat messages using NVIDIA NIM and saving history.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    try:
        data = json.loads(request.body)
        messages = data.get('messages', [])
        system_prompt = data.get('system_prompt', '')
        agent_id = data.get('agent_id')
        category = data.get('category')
        
        if not settings.NVIDIA_API_KEY:
            return JsonResponse({'error': 'NVIDIA API Key not configured.'}, status=500)
        
        # Save User Message to DB
        last_user_msg = messages[-1]['content']
        ChatMessage.objects.create(
            agent_id=agent_id,
            category=category,
            role='user',
            content=last_user_msg
        )

        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=settings.NVIDIA_API_KEY
        )
        
        full_messages = [{'role': 'system', 'content': system_prompt}] + messages
        
        completion = client.chat.completions.create(
            model=settings.NVIDIA_MODEL,
            messages=full_messages,
            temperature=0.7,
            max_tokens=1024,
        )
        
        response_text = completion.choices[0].message.content
        
        # Save Assistant Response to DB
        ChatMessage.objects.create(
            agent_id=agent_id,
            category=category,
            role='assistant',
            content=response_text
        )

        return JsonResponse({'response': response_text})
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

