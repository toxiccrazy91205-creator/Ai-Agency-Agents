from django.db import models

class ChatMessage(models.Model):
    """
    Stores chat messages for different agents.
    """
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]
    
    agent_id = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.agent_id} - {self.role}: {self.content[:50]}"
