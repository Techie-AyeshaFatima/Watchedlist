# WatchedList

By AYESHA FATIMA

Video overview: <[URL HERE](https://youtu.be/YpCvoQmPlpM)>

WatchedList is a web application that allows users to search for movies or dramas and categorize them into watchlist, watched list, or dropped list. This project was developed as part of the CS50W capstone project.

## Purpose

The purpose of WatchedList is to provide users with a convenient and organized way to manage their movie and drama viewing experiences. By allowing users to search for titles, categorize them into watchlist, watched list, or dropped list, and rate them, WatchedList aims to enhance the user's ability to keep track of their entertainment preferences and viewing history. The application leverages the OMDb API to offer detailed information about each title, making it easier for users to discover new content and make informed decisions about what to watch next.

## Distinctiveness and Complexity

WatchedList stands out from other projects in the CS50W course due to its unique combination of features and the challenges involved in its implementation. Unlike other projects, WatchedList integrates the OMDb API to provide users with detailed information about movies and dramas. This required learning how to interact with an external API, handle API requests, and process the returned data.

One of the most challenging aspects of this project was implementing the star rating system. This feature required a deep understanding of JavaScript to create an interactive and user-friendly rating interface. Additionally, integrating the rating system with the Django backend to store and retrieve user ratings added another layer of complexity.

The project also emphasizes a mobile-responsive design, ensuring that users can access and use the application seamlessly on various devices. This required careful consideration of CSS and Bootstrap to create a flexible and adaptive layout.

## Features

- Search for movies and dramas using the OMDb API
- Add movies and dramas to watchlist, watched list, or dropped list
- View detailed information about movies and dramas
- Implement star ratings for movies and dramas
- Mobile-responsive design

## Technologies Used

### Backend
- Django
- Python

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### API
- OMDb API

## File Structure
```
├── capstone/  -> core application
│   ├── __pycache__
│   ├── asgi.py  -> asgi interface configuration
│   ├── __init__.py
│   ├── wsgi.py
│   ├── settings.py
│   └── urls.py  -> global urls mapping
├── watchedlist/  -> main app to manage the website as a whole
│   ├── __pycache__
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_userfeedback.py
│   │   └── 0003_userfeedback_created_at.py
│   ├── static/
│   │   └── watchedlist/
│   │       ├── images/
│   │       │   ├── img0.png  -> image for user profile
│   │       │   ├── img1.jpg  -> image for homepage slider
│   │       │   ├── img2.jpg  -> image for homepage slider
│   │       │   ├── img3.jpg  -> image for homepage slider
│   │       │   ├── img4.jpg  -> image for homepage slider
│   │       │   └── img5.jpg  -> image for homepage slider
│   │       ├── item.js  -> handlers for putting an item in lists
│   │       ├── styles.css  -> register page
│   │       └── custom.css  -> search results
│   ├── templates/
│   │   └── watchedlist/
│   │       ├── layout.html  -> base template
│   │       ├── mylist.html  -> all lists page
│   │       ├── watchlist.html  -> watchlist template
│   │       ├── watchedlist.html  -> watched list page
│   │       ├── droppedlist.html  -> dropped list page
│   │       ├── index.html  -> index page
│   │       ├── item.html  -> detailed view page
│   │       ├── login.html  -> login page
│   │       ├── register.html  -> register page
│   │       └── results.html  -> search results page
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py  -> app models
│   ├── tests.py
│   ├── urls.py  -> urls to watchedlist
│   └── views.py  -> website views and api endpoints
├── manage.py
├── README.md  -> readme file with the instructions
└── requirements.txt  -> file that contains the project dependencies
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/watchedlist.git

2. Navigate to the project directory:
    ```bash
    cd watchedlist

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the development server:
    ```bash
    python manage.py runserver

## Usage
-Open your web browser and go to http://127.0.0.1:8000/.

- Use the search bar to find movies or dramas.

- Add them to your watchlist, watched list, or dropped list.

- View detailed information and rate the movies or dramas.

## Future Scope
WatchedList has the potential to evolve with several exciting features that can enhance user experience and engagement:

- *AI-Powered Recommendations*: Integrate AI algorithms to analyze users' watchlists, watched lists, and ratings to suggest personalized movie and drama recommendations. This feature can help users discover new content that aligns with their preferences and viewing history.

- *Public Lists*: Allow users to share their watchlists, watched lists, and dropped lists publicly. Other users can view these lists, follow them, and get inspired by the recommendations. This feature can foster a sense of community and enable users to explore content curated by others.

- *Social Features*: Introduce social features such as comments, likes, and ratings on public lists. Users can interact with each other's lists, share their thoughts, and provide feedback, creating a more engaging and interactive platform.

- *Enhanced Search Filters*: Implement advanced search filters to help users find movies and dramas based on specific criteria such as genre, release year, rating, and more. This can make the search experience more efficient and tailored to users' preferences.

- *User Profiles*: Create user profiles where individuals can showcase their favorite movies, dramas, and ratings. Profiles can also include personalized recommendations and a summary of their viewing habits.

- *Notifications and Reminders*: Add a notification system to alert users about new releases, upcoming episodes, and recommendations based on their watchlists. Reminders can help users keep track of their viewing schedules and never miss out on their favorite content.

- *Integration with Streaming Services*: Integrate with popular streaming services to provide direct links to watch movies and dramas. This can streamline the viewing experience and make it easier for users to access content from various platforms.

## Acknowledgements
- CS50W for providing the course and resources.
- OMDb API for providing the movie and drama data.