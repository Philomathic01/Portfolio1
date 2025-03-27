from django.shortcuts import render

def home(request):
    projects = [
        {
            'title': "Neural Network Vision System",
            'description': "Developed a computer vision system for real-time object detection using custom CNN architecture.",
            'image': "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-4.0.3",
            'github_url': "#",
            'live_url': "#",
            'technologies': ["PyTorch", "OpenCV", "Python", "CUDA"]
        },
        {
            'title': "NLP Research Platform",
            'description': "Built a scalable platform for processing and analyzing large-scale text datasets.",
            'image': "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3",
            'github_url': "#",
            'live_url': "#",
            'technologies': ["TensorFlow", "BERT", "Docker", "AWS"]
        },
        {
            'title': "Reinforcement Learning Agent",
            'description': "Created an RL agent for autonomous decision-making in complex environments.",
            'image': "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3",
            'github_url': "#",
            'live_url': "#",
            'technologies': ["PyTorch", "Ray", "Python", "Redis"]
        }
    ]
    
    skills = [
        {
            'title': "Deep Learning",
            'description': "Expertise in CNN, RNN, Transformers, and custom neural network architectures",
            'icon_class': "fas fa-brain"
        },
        {
            'title': "MLOps",
            'description': "Experience with ML pipelines, deployment, and monitoring at scale",
            'icon_class': "fas fa-cogs"
        },
        {
            'title': "Research",
            'description': "Published papers in top ML conferences and journals",
            'icon_class': "fas fa-flask"
        },
        {
            'title': "Software Engineering",
            'description': "Strong foundation in software design patterns and best practices",
            'icon_class': "fas fa-code"
        },
        {
            'title': "Leadership",
            'description': "Led teams of engineers and researchers on complex ML projects",
            'icon_class': "fas fa-users"
        }
    ]
    
    return render(request, 'main/index.html', {'projects': projects, 'skills': skills})