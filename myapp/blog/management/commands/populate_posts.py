
from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post,Catagory
import random


class Command(BaseCommand):

    help = "To Poulate Post"
    
    def handle(self, *args:Any, **options:Any):
        
        
        Post.objects.all().delete()

        blog_posts = [
    {
        "Title": "Must Watch Anime",
        "Content": "Anime has become a global phenomenon, and 2023 has been an incredible year for anime enthusiasts. From action-packed shonen to heartwarming slice-of-life series, this list covers the top 10 must-watch anime of the year. Dive into shows like 'Attack on Titan: The Final Season,' 'Demon Slayer: Swordsmith Village Arc,' and 'Chainsaw Man.' Each anime is explained in detail, including plot summaries, character analysis, and why they stand out in 2023.",
        "catagory": "Anime"
    },
    {
        "Title": "The Evolution of Anime",
        "Content": "Anime has come a long way since its inception in the 1960s with classics like 'Astro Boy.' This post explores the evolution of anime, highlighting key milestones, influential creators, and how the medium has grown into a global cultural force. Learn about the rise of Studio Ghibli, the impact of streaming platforms like Crunchyroll, and the future of anime.",
        "catagory": "Anime"
    },
    {
        "Title": "The 10 Best Movies",
        "Content": "2023 has been a fantastic year for cinema, with groundbreaking films across genres. From Christopher Nolan's 'Oppenheimer' to Greta Gerwig's 'Barbie,' this list covers the top 10 movies of the year. Each film is reviewed in detail, including plot summaries, performances, and why they are worth watching.",
        "catagory": "Movies"
    },
    {
        "Title": "The Rise of Superhero Movies",
        "Content": "Superhero movies have dominated the box office for over a decade. This post explores the rise of Marvel and DC films, their impact on pop culture, and how they revolutionized storytelling in cinema. From 'Iron Man' to 'The Batman,' learn how these franchises reshaped Hollywood.",
        "catagory": "Movies"
    },
    {
        "Title": "Top 5 Open-World Games",
        "Content": "Open-world games offer endless exploration and immersive storytelling. This post highlights the top 5 open-world games of 2023, including 'The Legend of Zelda: Tears of the Kingdom,' 'Starfield,' and 'Hogwarts Legacy.' Each game is reviewed, with details on gameplay, graphics, and why they stand out.",
        "catagory": "Games"
    },
    {
        "Title": "The History of Video Games",
        "Content": "Video games have evolved dramatically since the days of 'Pong' in the 1970s. This post takes you through the history of gaming, covering key milestones like the rise of consoles, the birth of online gaming, and the advent of virtual reality. Learn how gaming became a multi-billion-dollar industry.",
        "catagory": "Games"
    },
    {
        "Title": "The Most Exciting Sports Events of 2023",
        "Content": "2023 has been a thrilling year for sports fans, with events like the FIFA Women's World Cup, the NBA Finals, and the Wimbledon Championships. This post covers the most exciting sports events of the year, including highlights, key players, and memorable moments.",
        "catagory": "Sports"
    },
    {
        "Title": "The Science of Sports",
        "Content": "Technology is revolutionizing sports, from wearable fitness trackers to AI-powered analytics. This post explores how innovations like VAR in soccer, Hawk-Eye in tennis, and performance-tracking devices are enhancing athlete performance and fan experiences.",
        "catagory": "Sports"
    },
    {
        "Title": "The Future of AI",
        "Content": "Artificial Intelligence (AI) is transforming industries, from healthcare to entertainment. This post delves into the latest advancements in AI, including ChatGPT, self-driving cars, and AI-generated art. Learn how AI is shaping the future and what it means for society.",
        "catagory": "Technology"
    },
    {
        "Title": "Top 10 Gadgets of 2023",
        "Content": "2023 has seen the release of groundbreaking gadgets, from foldable smartphones to advanced VR headsets. This post reviews the top 10 gadgets of the year, including their features, pros, and cons, and why they are worth your attention.",
        "catagory": "Technology"
    },
    {
        "Title": "Why 'One Piece' is the GOAT",
        "Content": "With over 1,000 episodes, 'One Piece' is one of the longest-running anime series. This post explores why it remains so popular, diving into its rich storytelling, memorable characters, and the themes of adventure and friendship that resonate with fans worldwide.",
        "catagory": "Anime"
    },
    {
        "Title": "The Best Anime Movies of All Time",
        "Content": "Anime movies like 'Spirited Away,' 'Your Name,' and 'Akira' have left a lasting impact on audiences. This post lists the best anime movies of all time, with detailed reviews and reasons why they are must-watches for any anime fan.",
        "catagory": "Anime"
    },
    {
        "Title": "How Streaming Platforms are Changing the Way We Watch Movies",
        "Content": "Streaming platforms like Netflix, Disney+, and Amazon Prime have revolutionized the movie industry. This post examines how these platforms are changing movie distribution, production, and consumption, and what it means for the future of cinema.",
        "catagory": "Movies"
    },
    {
        "Title": "The Best Indie Games",
        "Content": "Indie games offer unique and creative experiences. This post highlights the best indie games of 2023, including 'Hades II,' 'Sea of Stars,' and 'Cocoon.' Each game is reviewed, with insights into their gameplay, art style, and storytelling.",
        "catagory": "Games"
    },
    {
        "Title": "The Impact of Esports",
        "Content": "Esports has grown into a billion-dollar industry, with games like 'League of Legends' and 'Fortnite' leading the charge. This post explores the rise of esports, its impact on the gaming industry, and how it has become a mainstream form of entertainment.",
        "catagory": "Games"
    },
    {
        "Title": "The Greatest Moments",
        "Content": "From Michael Jordan's 'Flu Game' to Usain Bolt's world records, sports history is filled with unforgettable moments. This post revisits the greatest moments in sports history, celebrating the athletes and events that defined generations.",
        "catagory": "Sports"
    },
    {
        "Title": "How to Stay Fit",
        "Content": "Staying fit is essential for a healthy lifestyle. This post provides a beginner's guide to sports and fitness, covering tips on choosing the right sport, creating a workout routine, and staying motivated.",
        "catagory": "Sports"
    },
    {
        "Title": "The Role of Blockchain in Modern Technology",
        "Content": "Blockchain technology is more than just cryptocurrencies. This post explores its applications in industries like finance, healthcare, and supply chain management, and how it is shaping the future of technology.",
        "catagory": "Technology"
    },
    {
        "Title": "The Pros and Cons of Smart Home Devices",
        "Content": "Smart home devices like Amazon Echo and Google Nest are becoming increasingly popular. This post examines the pros and cons of these devices, including their convenience, privacy concerns, and impact on daily life.",
        "catagory": "Technology"
    },
    {
        "Title": "The Best Anime Soundtracks of All Time",
        "Content": "Anime soundtracks are known for their emotional depth and memorable melodies. This post lists the best anime soundtracks of all time, including works by composers like Yoko Kanno and Hiroyuki Sawano, and why they are so impactful.",
        "catagory": "Anime"
    }
]
        
        image_paths = [
    "post/images/1734508047-top_10_anime_2024_-_Homes247.jpg",
    "post/images/62a51cdd-a936-4562-9f71-3b03c1593085_1053x739.webp",
    "post/images/muhammx-aiman-dfreify-00066a11-078e-45ce-a755-d09381fa9f79.jpg",
    "post/images/2017-11_GQ_SuperheroRankings_3x2.webp",
    "post/images/bhrwxnnt9nm81.png",
    "post/images/vidya.webp",
    "post/images/TFP-Major-Sporting-Events-2023-UPDATE.jpg",
    "post/images/science_sports_web_banner.png",
    "post/images/The-Future-of-AI-and-Its-Impact-on-Humanity.webp",
    "post/images/10-COOL-GADGETS-TO-LOOK-OUT-FOR-IN-2023.png",
    "post/images/The_GOAT.webp",
    "post/images/wp6265448.jpg",
    "post/images/why-are-people-cancelling-netflix.webp",
    "post/images/e18ed-16427882442356-1920.webp",
    "post/images/VMX-blog-game-or-sport-navigating-through-the-esports-identity-maze.webp",
    "post/images/maxresdefault.jpg",
    "post/images/main-2.jpg",
    "post/images/1731441463601.png",
    "post/images/Smart-Home-infographics-pic-1.jpg",
    "post/images/1335171.png"
]

        
        users = User.objects.all()
        
        for post,image in zip(blog_posts,image_paths):
            user = random.choice(users)
            catagory, created = Catagory.objects.get_or_create(catagory_name=post['catagory'])
            Post.objects.create(title = post['Title'],content = post['Content'],is_published = True,catagory = catagory,user = user,image = image)

        self.stdout.write(self.style.SUCCESS("Sucessfully inserted !!"))

