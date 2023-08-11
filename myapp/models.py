from django.db import models

# Create your models here.
from django.db import models

class Conversation(models.Model):
    user_input = models.TextField()
    assistant_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'myapp'
    def __str__(self):
        return f"User: {self.user_input[:50]} | Assistant: {self.assistant_response[:50]}"
