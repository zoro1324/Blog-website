from django.core.management.base import BaseCommand
from blog.models import AboutUs
from typing import Any

class Command(BaseCommand):

    def handle(self, *args, **options):
        AboutUs.objects.all().delete()
        content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - Zoro's Blog</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 800px; margin: auto; padding: 40px; }
        .header { text-align: center; margin-bottom: 30px; }
        body { background-color: #efe2da; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>About Us</h1>
            <p>Welcome to Zoro's Blog - Where Passion Meets Expression!</p>
        </div>
        <p>Zoro's Blog is a space where we dive deep into anime, gaming, and problem-solving, bringing insightful discussions and engaging content to like-minded enthusiasts. Founded by <strong>Naveen Kumar</strong>, a passionate blogger and tech enthusiast from Coimbatore, our goal is to connect, inspire, and entertain our readers.</p>
        <h2>Our Mission</h2>
        <p>We aim to create a vibrant community for anime lovers, gamers, and tech enthusiasts, providing thought-provoking content and useful insights into the world of technology, development, and entertainment.</p>
        <h2>Meet the Creator</h2>
        <p>Naveen Kumar, a college student and Python developer, started this blog as a way to share his knowledge and passion for anime, gaming, and coding. Whether it’s exploring the best anime storylines, reviewing the latest games, or solving complex coding problems, Zoro's Blog is the ultimate space for expression and discussion.</p>
        <h2>Join the Community</h2>
        <p>Be part of our journey! Connect with us, share your thoughts, and explore our latest posts. Whether you are a hardcore anime fan, an avid gamer, or a coding geek, there’s something for everyone at Zoro's Blog.</p>
    </div>
</body>
</html>

        """
        image = "blog/aboutus/Roronoa_Zoro__One_piece-Photoroom.png"
        AboutUs.objects.create(content = content,image=image)
        print("Updated")
        
