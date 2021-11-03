from django.db import models

# Create your models here.

class newResource(models.Model):
    res_type = [('sensor', 'sensor'),('actuator', 'actuator'),]
    input_type = [('sensor', 'sensor(no input)'),('switch', 'switch'), ('slider', 'slider')]
    resource = models.CharField(max_length=8, choices=res_type, default='sensor')
    resource_input = models.CharField(max_length=8, choices=input_type, default='sensor')
    name = models.CharField(max_length = 30)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    
    
    
    
