<div align="center">

# Jot <!-- omit in toc -->
## A 5 minute journal app  <!-- omit in toc -->

[Testing Documentation](link)

[Live Site](link)

<br>

![Website Mockup](link)

</div>

# Table of contents <!-- omit in toc -->
- [1. Website Information](#1-website-information)
- [2. UX](#2-ux)
  - [2.1 Strategy](#21-strategy)
  - [2.2 Scope](#22-scope)
  - [2.3 Structure](#23-structure)
  - [2.4 Skeleton](#24-skeleton)
  - [2.5 Surface](#25-surface)
- [3. Technologies Used](#3-technologies-used)
- [4. Testing](#4-testing)
- [5. User Story](#5-user-story)
- [6. Deployment](#6-deployment)
  - [Heroku Deployment](#heroku-deployment)
- [7. Credits and Acknowledgments](#7-credits-and-acknowledgments)

## 1. Website Information 
Business goals: 
* Allow user to register for an account
* Allow user to log in to previously registered account
* Allow user to view previously posted entries
* Allow user to create a new book review entry
* Allow user to edit book review entries
* Allow user to delete a book review entry if they are logged in 
* Allow user to log out of account
* Allow user to access external social media pages

### 1.1 Website Sections: <!-- omit from toc -->
1. Home
2. Register 
3. Log in
4. Profile
5. Create Entry
6. Edit Entry

---

## 2. UX 

Whilst designing and creating this website I have taken into account the five planes of UX design, strategy, scope, structure, skeleton and surface.

### 2.1 Strategy
This plane is the first, it involves identifying the goals and objectives of the site and the user. By identifying these first, design decisions can be made that meet these goals.

**User and site goals**
Target users for Jot:
* Ages 13+ (I tried to style the web application in order to appeal to a broad age group)
* Gender non specific
* People who enjoy reading a wide variety of genres
* People who enjoy reviewing books they have read
* People who enjoy reading other's reviews of books

First time and returning user goals: 
* I want to register for an account.
* I want to log in and log out of my account.
* I want to be able to create new entries.
* I want to be able to find and read previous entries.
* I want to be able to edit previous entries.
* I want to be able to delete previous entries.
* I want to easiy and intuitively find my way around the site.

While the app is a book review platform, my goal was to create something that was incredibly simple but provided an enjoyable and aesthetically pleasing user experience with little to no guess work in regards to input and navigation features.

### 2.2 Scope - Unfinished
The second plane of UX looks at the **scope** of the website. What does the user have to do in order to reach both the user and the site owners goals for the website.

#### Features <!-- omit in toc -->

| Landing Page |A simple landing page navigating users to either register or log in to their accounts|
|:---:|---|
|`Nav Bar`|A responsive navigation bar that allows for easy navigation to every page of the site|
|`H1`|Used for the app name|
|`H2`|Used for the journal tagline|
|`Large Button`|A button navigating to the register page|
|`Large Button`|A button navigating to the log in page|
|`Small Button`|A button to sort entries by 'most recent'|
|`Small Button`|A button to sort entries by 'book title'|
|`Small Button`|A button to sort entries by 'author name'|
|`Footer`|A simple footer section with site creator info, a text link and social media links|

| Register |A page that allows the user to register for an account|
|:---:|---|
|`Nav Bar`|A responsive navigation bar that allows for easy navigation to every page of the site|
|`H3`|Used for the title of the page|
|`Form`|A simple form allowing users to input a username and password in order to register for an account|
|`Large Button`|A button to initiate registration|
|`Link`|A link to the log in page for users already registered|
|`Footer`|A simple footer section with site creator info, a text link and social media links|

| Log In |A page that allows the user to log in to their previously registered account|
|:---:|---|
|`Nav Bar`|A responsive navigation bar that allows for easy navigation to every page of the site|
|`H1`|Used for the title of the page|
|`Form`|A simple form allowing users to input their username and password in order to log in to their account|
|`Large Button`|A button to initiate log in|
|`Link`|A link to the register page for users not yet registered|
|`Footer`|A simple footer section with site creator info, a text link and social media links|

|Profile|A simple navigation page for users that have logged in|
|:---:|---|
|`Nav Bar`|A responsive navigation bar that allows for easy navigation to every page of the site|
|`H1`|Used for the title of the page (a user specific message generated on log in)|
|`Large Button`|A button navigating user to index page (home of all entries)|
|`Large Button`|A button navigating user to the create entry page|
|`Large Button`|A button logging user out and redirecting to log in page|
|`Footer`|A simple footer section with site creator info, a text link and social media links|

|Create entry|A form for users to fill in to create a new book review entry|
|:---:|---|
|`Nav Bar`|A responsive navigation bar that allows for easy navigation to every page of the site|
|`H3`|Used for the title of the page|
|`Form`|A form for users to fill in to create a new review entry| 
|`Large Button`|A submit button that saves new entry to database|
|`Footer`|A simple footer section with site creator info, a text link and social media links|

|Edit entry|A form for users to fill in to edit an existingbook review entry|
|:---:|---|
|`Nav Bar`|A responsive navigation bar that allows for easy navigation to every page of the site|
|`H3`|Used for the title of the page|
|`Form`|A form for users to fill in to create a new review entry| 
|`Large Button`|A cancel button that redirects user back to index page|
|`Large Button`|A submit button that saves edited entry to database|
|`Footer`|A simple footer section with site creator info, a text link and social media links|

|Log out|A function that allows user to log out of account|
|:---:|---|
|`Button` & `Nav Link`|Featured in both nav bar and on profile page, this does not load a page, just initiated a function that logs the session user out of their account and redirects user back to log in page|

|Flashes|A temporary message at the top of the page dependant on user interaction|
|:---:|---|
|`Flash Message`|When the user interacts with certain areas of the page a flash message is displayed at the top of the page. (i.e When the user successfully logs out a flash message appears saying 'You have been logged out') These messages lets the user know their desired action has been completed.|

### 2.3 Structure - Unfinished
The structure plane deals with the organising and arrangment of elements within the user interface. Creating userflows to define how the user will interact with the page. A big goal of the structure plane is to ensure that the users can easily find and access the information they need.

I created a userflow diagram to show how the user will interact with each page on the site. Since my goal was for the app to be simple I tried to keep each page and action within as few clicks as possible.

<details><summary>Click here for userflow</summary>

![Userflow](link)

</details>

### 2.4 Skeleton - Unfinished
This plane is a more refined view of the user interface. Looking at the layout and visual hierarchy to ensure the site is both visually appealing and functional. I created a set of wireframes for different screen sizes, this is a simplified version of the final product, removing colour, typography, imagery to create a basic view of website and establish the layout.

| Mobile Wireframes | Desktop Wireframes |
|:---:|:---:|
|![Mobile Wireframes](/static/images/readme-img/wireframe-mobile.png)|![Tablet and Desktop Wireframes](/static/images/readme-img/wireframe-large.png) |

*Note: Some areas have changed between the wireframes and the final product, this is either due to making the page easier to navigate or an added function later in development.*

### 2.5 Surface - Unfinished
The surface plane is the last layer and deals with the aesthetics of the user interface. This includes colour palettes, typography, graphics and visual style. The goal of this plane is to create a page that is visually pleasing and engaging for the user.

| Type | Image | Description|
|:---:|---|---|
|Typography - Title|![google fonts](/static/images/readme-img/typography-title.png)| I chose to use a bold but readable font that aligned with the idea of writing and books. I used this only for title text and logo text|
|Typography - Main Text|![google fonts](/static/images/readme-img/typography-main.png)| I chose to use a simple sans serif font for the rest of the text on the page so as to keep the text easy to read |
|Colours|![Colour Palette Grey](/static/images/readme-img/colours-grey.png)| I used the built in class name colour palettes from materialize to make colour picking and styling easier. |
|Colours|![Colour Palette Red](/static/images/readme-img/colours-red.png)| I used the built in class name colour palettes from materialize to make colour picking and styling easier. |

---

## 3. Technologies Used

### Languages <!-- omit in toc -->
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): Used to create the basic structure of the webpage.

[CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics): Used to style the content within the webpage.

[JavaScript](https://www.javascript.com/): Used with Materialize CSS in order to create a responsive drop down nav bar on mobile.

[Python](https://www.python.org/): Used to link app to database and complete a variety of functions depending on user interactions in order to run the app.

[Markdown](https://www.markdownguide.org/): Used to format README.md and TESTING.md.


### Libraries <!-- omit in toc -->
![Materialize CSS](https://img.shields.io/badge/materialize_css-white?style=flat)
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

[Materialize CSS](https://materializecss.com/): Used to style site and add interactive components (eg. navbar and buttons)

[jQuery](https://jquery.com/): Used to simplify and streamline JS code.

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/): Used to create generatable page templates and iterating statements.

### Design <!-- omit in toc -->
![Static Badge](https://img.shields.io/badge/Google_Fonts-white?style=flat-plastic&logo=google&logoColor=black)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

[Google Fonts](https://fonts.google.com/): Used to add in specific fonts to the webpage.

[Figma](https://www.figma.com/): Used to create userflow and wireframes.

### Other <!-- omit in toc -->
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

[MongoDB](https://www.mongodb.com/): Used as linked database to store user information and user input

[Heroku](https://www.heroku.com/home): Used connect front and back end and deploy site
---

## 4. Testing
[Click to view testing documentation](testing.md)

---

## 5. Deployment
### GitHub pages deployment <!-- omit in toc -->
Once this is complete you should be able to view the webpage online, this is updated every so often which allows the user to see any changes in almost real time.

*Log in to GitHub*
- In your Repository section, select the project repository that you want to deploy
- In the menu located at the top of this section, click 'Settings'
- Select 'Pages' on the left-hand menu - this is around halfway down
- In the source section, select branch 'Master' and save
- The page is then given a site URL which you will see above the source section

### Heroku Deployment

**Creating an Application with Heroku**

I followed the below steps using the Code Institute Flask Walkthrough:

1. The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies `pip3 freeze --local > requirements.txt`.
2.  Please note this file should be added to a `.gitignore` file to prevent the file from being committed. 
3. A `Procfile` is also required that specifies the commands that are executed by the app on startup.
4. Go to Heroku.com and log in; if you do not already have an account then you will need to create one.
5. Select `Create New App`.
6. Enter a name for your new app, this needs to be a unique name (adding initials/your name at the end will help), you will be prompted if you need to change it.
Select the region you are working in.

**Heroku Deployment using website In the Deploy tab:**

*Connect your Heroku account to your Github Repository following these steps:*

1. Click on the `Deploy` tab and choose Github-Connect to Github.
2. Enter the GitHub repository name and click on `Search`.
3. Choose the correct repository for your application and click on `Connect`.
4. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the Deploy Branch button whenever you want a change made.


In the Settings tab, click on Reveal Config Vars and set the fo

|Deployment Type|Screenshot|Description
|:--:|:--:|:--:|
|Automatic|![screenshot of Heroku environment variables](static/images/readme-images/heroku-config.png)|*In Heroku Settings*: You will need to set your Environment Variables within the config settings by clicking `Reveal Config Vars` before allowing automatic deployment - this is a key step to ensuring your application is deployed properly.|
|Manual|![screenshot of manual deployment section](static/images/readme-images/heroku-manual-deploy.png)|*In deploy tab*: You can also opt to manually deploy the project which will initiate a build.|

5. Once you have chosen your deployment method and have clicked `Deploy Branch` your application will be built and you should see the below `View` button, click this to open your application:

![Heroku manual deploy view button screenshot](static/images/readme-images/heroku-deploy-view.png)


**Heroku CLI deployment** 

It's also possible to log in, commit and deploy your app via the command line:

1. Login to Heroku via the CLI using heroku login -i
2. Enter your email and password
![Heroku CLI login screenshot](static/images/readme-images/heroku-cli-login.png)
3. Using the following commands in the terminal you can commit and push your files to both Heroku and Github:
    
    git add -A

    git commit -m "INSERT COMMIT MESSAGE"
    
    git push

---

## 6. Credits and Acknowledgments
- [Google Fonts](https://fonts.google.com/)
  * Used to find fonts across the site.
- [Figma](https://www.figma.com/)
  * Used to create wireframes.
- [ui.dev](https://ui.dev/amiresponsive)
  * Used to create a mockup of web page on various screen sizes.
- [Font-size Clamp Generator](https://clamp.font-size.app/?config=eyJyb290IjoiMTYiLCJtaW5XaWR0aCI6IjMyMHB4IiwibWF4V2lkdGgiOiIxMDI0cHgiLCJtaW5Gb250U2l6ZSI6IjI0cHgiLCJtYXhGb250U2l6ZSI6IjYwcHgifQ%3D%3D): Used to create responsive text sizes.
  * Used for responsive text.
- [Materialize CSS](https://materializecss.com/)
  * Used to create fully responsive navbar, buttons and images.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
  * Used for testing.
- [JShint](https://jshint.com/)
  * Used for testing.
  
---