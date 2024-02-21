[Return to README](https://github.com/lrchnnng/parrot-quiz/blob/main/README.md)

---
# Testing <!-- omit in toc -->
- [Automated vs Manual Testing](#automated-vs-manual-testing)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [Known bugs and fixes](#known-bugs-and-fixes)

---

## Automated vs Manual Testing

Automated testing and manual testing, when used in combination, are able to achieve a greater level of testing coverage. Automated testing is good for repetitive and critical tasks, while manual testing is good for new or changing requirements and exploratory testing.

---

<div align="center">

## Manual Testing

</div>

---

Manual testing allows the tester to explore the site and using experience and creativity to find any issues within the site. It also takes into account flexibility and context, manual testing paramaters can be changed quickly depending on the requirements. The tester can also take into account the prospective users and their knowledge of the system in order to execute tests that are relevant.  

|Responsivity | Mobile S (320px)| Mobile L (425px)| Tablet (768px) | Desktop (1024px)|
|---|:---:|:---:|:---:|:---:|
|Responsive UI Components|✓|✓|✓|✓|
|Responsive Text|✓|✓|✓|✓|
|Responsive Form|✓|✓|✓|✓|
|Responsive Button Placement|✓|✓|✓|✓|
|Responsive Nav Bar|✓|✓|✓|✓|
|Responsive Footer|✓|✓|✓|✓|

|Nav Bar Testing|Yes/No|
|---|:---:|
|Nav bar text and styles are loaded|✓|
|Nav bar collapse appears up to medium sized screens|✓|
|Nav links work as intended|✓|
|Nav logo directs user to index page|✓|
|If user is **not** in session, nav bar shows `Home`, `Register` and `Log In` links|✓|
|If user is in session, nav bar shows `Home`, `Profile`, `Create Entry` and `Log Out` links|✓|
|`Home`link directs user to index page|✓|
|`Register` link directs user to Register page|✓|
|`Log In` link directs user to Log In page|✓|
|`Profile` link directs user to Profile page|✓|
|`Create Entry` link directs user to Creat Entry page|✓|
|`Log Out` link logs user out and redirects to Log In page and displays a flash message at top of page|✓|

|Footer Testing|Yes/No|
|---|:---:|
|Fonts and styling are loaded|✓|
|Logo directs user to index page|✓|
|`Instagram` link directs user to instagram site in a separate tab|✓|
|`Facebook` link directs user to facebook site in a separate tab|✓|
|`Pinterest` link directs user to pinterest site in a separate tab|✓|

|Index Page Testing|Yes/No|
|---|:---:|
|Font and styling are loaded|✓|
|Components are loaded|✓|
|`Register` button directs user to register page|✓|
|`Log In` button directs user to log in page|✓|
|`Sort by most recent` button sorts posts by most recent first|✓|
|`Sort by book title` button sorts posts by book title in alphabetical order|✓|
|`Sort by author` button sorts posts by author name in alphabetical order|✓|
|Sort buttons display as disabled once selected|✓|
|`Edit` button redirects user to the 'Edit Entry' Page|✓|
|`Delete` button deletes the post|✓|
|Flash message appears at top of page describing the sort order|✓|
|If user is **not** in session `Register` and `Log In` buttons are shown|✓|
|If user is in session only `Create Entry` button is shown|✓|
|If user is **not** in session, `Edit` and `Delete` buttons are **not** shown|✓|
|If user is in session, `Edit` and `Delete` buttons are shown|✓|

|Register Page Testing|Yes/No|
|---|:---:|
|Fonts and styles are loaded|✓|
|Username input does not accept under 5 characters|✓|
|Username input does not accept over 15 characters|✓|
|Username input does not accept special characters|✓|
|Password input does not accept under 5 characters|✓|
|Password input does not accept over 15 characters|✓|
|Password input does not accept special characters|✓|
|`Register` button directs user to profile page|✓|
|`Log In Here` link redirects user to Log In page|✓|
|Flash message appears at top of page confirming successful registration|✓|

|Log In Page Testing|Yes/No|
|---|:---:|
|Fonts and styles are loaded|✓|
|Username input does not accept under 5 characters|✓|
|Username input does not accept over 15 characters|✓|
|Username input does not accept special characters|✓|
|Password input does not accept under 5 characters|✓|
|Password input does not accept over 15 characters|✓|
|Password input does not accept special characters|✓|
|`Log In` button directs user to profile page|✓|
|`Register Here` link redirects user to Log In page|✓|

|Profile Page Testing|Yes/No|
|---|:---:|
|Fonts and styles are loaded|✓|
|Personalised message with session user username included|✓|
|`View Entries` button directs user to index page|✓|
|`Create Entry` button directs user to Create Entry page|✓|
|`Log Out` button logs user out and redirects user to log in page with a flash message at top of page confirming successful log out|✓|

|Create Entry Page Testing|Yes/No|
|---|:---:|
|Fonts and styles are loaded|✓|
|Icons are loaded|✓|
|`Review Title` input does not accept under 5 characters|✓|
|`Review Title` input does not accept over 50 characters|✓|
|`Book Title` input does not accept under 3 characters|✓|
|`Book Title` input does not accept over 100 characters|✓|
|`Author Name` input does not accept under 3 characters|✓|
|`Author Name` input does not accept over 50 characters|✓|
|`Book Genre` dropdown list is loaded|✓|
|`Book Genre` input displays genre once selected|✓|
|`Review` input does not accept under 5 characters|✓|
|`Review` input does not accept over 1000 characters|✓|
|`Publish Date` prompts a calendar selection|✓|
|`Publish Date` calendar text is all visible and easily readable|✓|
|`Publish Date` month dropdown selection functions correctly|✓|
|`Publish Date` year dropdown selection functions correctly|✓|
|`Publish Date` input displays selected date on form|✓|
|`Publisher Name` input does not accept under 3 characters|✓|
|`Publisher Name` input does not accept over 50 characters|✓|
|`Recommend Select Lever` functions correctly|✓|
|`Review Date` prompts a calendar selection|✓|
|`Review Date` calendar text is all visible and easily readable|✓|
|`Review Date` input displays selected date on form|✓|
|`Review Date` month dropdown selection functions correctly|✓|
|`Review Date` year dropdown selection functions correctly|✓|
|`Edit Entry` button saves form content to MongoDB|✓|
|`Edit Entry` button redirects user to index page|✓|
|Flash message appears at top of index page confirming successful creation of entry|✓|
|`Edit Entry` does not redirect if any input field is empty|✓|


|Edit Entry Page Testing|Yes/No|
|---|:---:|
|Fonts and styles are loaded|✓|
|Icons are loaded|✓|
|Previous input values are added to the form for user to change at will|✓|
|`Review Title` input does not accept under 5 characters|✓|
|`Review Title` input does not accept over 50 characters|✓|
|`Book Title` input does not accept under 3 characters|✓|
|`Book Title` input does not accept over 100 characters|✓|
|`Author Name` input does not accept under 3 characters|✓|
|`Author Name` input does not accept over 50 characters|✓|
|`Book Genre` dropdown list is loaded|✓|
|`Book Genre` input displays genre once selected|✓|
|`Review` input does not accept under 5 characters|✓|
|`Review` input does not accept over 1000 characters|✓|
|`Publish Date` prompts a calendar selection|✓|
|`Publish Date` calendar text is all visible and easily readable|✓|
|`Publish Date` month dropdown selection functions correctly|✓|
|`Publish Date` year dropdown selection functions correctly|✓|
|`Publish Date` input displays selected date on form|✓|
|`Publisher Name` input does not accept under 3 characters|✓|
|`Publisher Name` input does not accept over 50 characters|✓|
|`Recommend Select Lever` functions correctly|✓|
|`Review Date` prompts a calendar selection|✓|
|`Review Date` calendar text is all visible and easily readable|✓|
|`Review Date` input displays selected date on form|✓|
|`Review Date` month dropdown selection functions correctly|✓|
|`Review Date` year dropdown selection functions correctly|✓|
|`Cancel` button redirects user back to index without saving changes|✓|
|`Edit Entry` button saves form content to MongoDB, rewriting previous entry|✓|
|`Save Entry` button redirects user to index page|✓|
|Flash message appears at top of index page confirming successful edit of entry|✓|
|`Save Entry` does not redirect if any input field is empty|✓|


## User Story Testing
1. I want to register for an account.
  
|Nav Bar|Index Page|Register Page|
|---|---|---|
|![Registration link in nav bar](/static/images/testing-img/userstory-nav1.png)|![Registration Button on index page](/static/images/testing-img/userstory-index-button1.png)|![Register Page](/static/images/testing-img/userstory-register.png)|
|User can find the registration page in the nav bar|User can also navigate to the registration page by clicking the `REGISTER` button on the Index page|User can input a username and password and click the register button in order to create an account. By clicking the `REGISTER` button the user's username and password will be saved to the database and the user will be redirected to the Profile page.|


2. I want to log in and log out of my account.

|Nav Bar|Index Page|Log In Page|
|---|---|---|
|![Log In link in nav bar](/static/images/testing-img/userstory-nav1.png)|![Log In Button on index page](/static/images/testing-img/userstory-index-button1.png)|![Log In Page](/static/images/testing-img/userstory-login.png)|
|User can find a link to the Log In page in the nav bar| User can also navigate to the Log In page by by clicking the `LOG IN` button on the Index page|Once the user inputs their preregistered username and password and clicks the `LOG IN` button they will be redirected to the Profile page.|

3. I want to be able to create new entries.

|Nav Bar|Index Page|Profile Page|
|---|---|---|
|![Nav Bar - logged in](/static/images/testing-img/userstory-nav2.png)|![Index Page - logged in](/static/images/testing-img/userstory-index-button2.png)|![Create Entry Page](/static/images/)|
|Once the user is logged in, the nav bar will show a link to the Create Entry page|The user will also have the `CREATE ENTRY` button available to them which will redirect to the Create Entry page|Once logged in the user will be redirected to the Profile page. This page has a `CREATE ENTRY` button that will navigate to the Create Entry page|

|Create Entry Page|Save Entry Button|Saved Entry|
|---|---|---|
|![Create Entry Page](/static/images/testing-img/userstory-create.png)|![Create entry save button](/static/images/testing-img/userstory-save-button.png)|![Index page entry](/static/images/testing-img/userstory-index-entry.png)|
|This page allows the user to fill in the form in order to create an entry.|Once the form is complete and all fields are filled the user can click the `SAVE ENTRY` button which will save the entry to the database|After the entry is saved it will be displayed along with other entries on the Index page.|


4. I want to be able to find and read previous entries.

|Index Page - Entry|Nav Bar|Profile|
|---|---|---|
|![Index page - Entry](/static/images/testing-img/userstory-index-entry.png)|![Nav Bar](/static/images/testing-img/userstory-nav2.png)|![Profile Page](/static/images/testing-img/userstory-profile.png)|
|User can view previous entries by scrolling down on the index page. There are also clickable buttons to `SORT BY MOST RECENT`, `SORT BY BOOK TITLE` and `SORT BY AUTHOR`.|Users can navigate to the Index page through a clickable link in the nav bar (visible to users logged in or not) or by clicking the 'Jot' logo in the nav bar and footer.|Users can also click `VIEW EDNTRIES` in the Profile page to be redirected to the Index page.|

5. I want to be able to edit previous entries.

|Index Page - Entry|Edit Entry Page|Edit Entry Button|
|---|---|---|
|![Edit Entry button - Index page](/static/images/testing-img/userstory-index-entry.png)|![Edit entry page](/static/images/testing-img/userstory-edit.png)|![Edit entry and cancel buttons](/static/images/testing-img/userstory-edit-button.png)|
|Users are able to edit entries by clicking the lighter `EDIT ENTRY` (the button with the pencil icon) button on the bottom left of the post.|The edit entry page will show a prefilled form that allows the user to edit the previously saved input fields.|Once the form has been completed and all fields have been filled the user can click the `EDIT ENTRY` button to save the entry. This overwrites the previously saved entry within the database. The user also has the option to select `CANCEL` button. Both buttons redirect the user back to the Index page.|

6. I want to be able to delete previous entries.

|Index Page - Entry|
|---|
|![Delete button - Index page](/static/images/testing-img/userstory-index-entry.png)|
|User has the option to delete any post as long as they are logged in. By clicking the `Delete` button (the button with the bin icon) the post is deleted from the database and removed from the index page.|

7. I want to easily and intuitively find my way around the site.

|Nav Bar - Not Logged In|Nav Bar - Logged In|Profile Page|
|---|---|---|
|![Nav bar logged out](/static/images/testing-img/userstory-nav1.png)|![Nav bar logged in](/static/images/testing-img/userstory-nav2.png)|![Profile Page](/static/images/testing-img/userstory-profile.png)|
|When the user is not logged in they have the option to navigate to either the Index page, Register page or Log In page.|When the user is logged in they can navigate to the Index page, Profile page, Create Entry page or Log Out of their account.|When the user is logged in they have access to their profile page which has three buttons. These buttons allow navigation to the Index page (`VIEW ENTRIES`), Create Entry page and to Log Out of the account.|


---

<div align="center">

## Automated Testing

</div>

Automated tests are repeatable and reliable as there is limited risk for human error. It allows for testing on both a small and a large scale in a quick and efficient manner. Automated testing might be used to test the performance of a site in order to ensure that it can handle page loading.


### HTML and CSS Validation <!-- omit in toc -->
### HTML <!-- omit in toc -->
[HTML Validation](https://validator.w3.org/nu/#textarea)
|Page|Errors|Explanation|Fixes|
|:---:|---|---|---|
|All pages but Base|Warning for missing `lang` attribute|A suggestion of the addition of `lang` attribute to declare the language of the document. Since I am using Jinja templating to extend the base template which includes this attribute this does not need to be included in the other pages|Warning Ignored|
|All pages|Bad Value, Parse Error & Text not allowed Error|The validator does not recognise the curly brackets used in the Jinja statements. Ignoring all of the errors that include the use of curly brackets there are no other issues.|Errors ignored|
|Index|Stray end tag `div`|An extra unused div tag found on line 24|Removed the stray div tag|
|Create Entry|Attribute `type` not allowed on element **textarea**|Using `type="textarea"` is not allowed on a textarea element|Type attribute removed|
|Edit Entry|Attribute `type` not allowed on element **textarea**|Using `type="textarea"` is not allowed on a textarea element|Type attribute removed|
|Log In|Unclosed element `div`|An unclosed div element found on line 35|Added missing closing `div` element|

### CSS <!-- omit in toc -->
[CSS Validation](https://validator.w3.org/nu/#textarea)

All pages passed CSS validation
![CSS validation](static/images/testing-img/css-validation.png)

### Lighthouse <!-- omit in toc -->

| Page | Test Results | Lighthouse Suggested Improvements |
|:---:|---|---|
|Index - Test 1|![First test index](/static/images/testing-img/lighthouse-index-test1.png)|Edit and delete buttons have no discernable name, I have fixed this by adding aria labels to the buttons in order to assist screen readers|
|Index - Test 2|![Second test index](/static/images/testing-img/lighthouse-index-test2.png)|Future goals: Create a custom 'disabled button' class style with higher contrast for the disabled sort button. Enable text compression and defer all non-critical JS and styles in order to stop resources from blocking the render.|
|---|---|---|
|Register - Test 1|![First test register](/static/images/testing-img/lighthouse-register-test1.png)|Future goals: Reduce unused JavaScript from MaterializeCSS|
|---|---|---|
|Log In - Test 1|![First test log in](/static/images/testing-img/lighthouse-login-test1.png)|Future goals: Reduce unused JavaScript from MaterializeCSS|
|---|---|---|
|Profile - Test 1|![First test profile](/static/images/testing-img/lighthouse-profile-test1.png)|Future goals: Defer all non-critical JS and styles in order to stop resources from blocking the render lowering the time it takes to load the page.|
|---|---|---|
|Create Entry - Test 1|![First test create entry](/static/images/testing-img/lighthouse-create-test1.png)|Issues with contrast between background and foreground, I have changed the 'Choose Genre' dropdown font colour, and the font colour of the switch lever labels|
|Create Entry - Test 2|![Second test create entry](/static/images/testing-img/lighthouse-create-test2.png)|Future goals: Reduce unused JavaScript and reduce initial server response time to increase performance. I would also find a way to add a label to the dropdown genre menu to improve accessability score.|
|---|---|---|
|Edit Entry - Test 1|![First test edit entry](/static/images/testing-img/lighthouse-edit-test1.png)|Issues with contrast between button colour and font colour for the cancel button, I have fixed this by changing the font colour|
|Edit Entry - Test 2|![First test edit entry](/static/images/testing-img/lighthouse-edit-test2.png)|Future goals: Reduce unused JavaScript and reduce initial server response time to increase performance. I would also find a way to add a label to the dropdown genre menu to improve accessability score.|

## WAVE Accessibility Evaluation

|Page|Result|Description|
|---|---|---|
|Index|![WAVE index](/static/images/testing-img/wave-index.png)|Known error: Disabled sort button contrast is too low and I would address this on a later iteration|
|Register|![WAVE register](/static/images/testing-img/wave-register.png)|Missing h1 element: I used a h3 element instead of a h1 element to make styling easier|
|Log In|![WAVE Log In](/static/images/testing-img/wave-login.png)|Missing h1 element: I used a h3 element instead of a h1 element to make styling easier. WAVE is flagging the 'Register Here!' link as a redundant link as there is also a link in the nav bar on the same page.|
|Profile|![WAVE Profile](/static/images/testing-img/wave-profile.png)|Missing h1 element: I used a h3 element instead of a h1 element to make styling easier.|
|Create Entry|![WAVE Create Entry](/static/images/testing-img/wave-create.png)|Missing form label: known error that would be addressed in later iterations of the app. Missing h1 element: I used a h3 element instead of a h1 element to make styling easier.|
|Edit Entry|![WAVE Edit Entry](/static/images/testing-img/wave-edit.png)|Missing form label: known error that would be addressed in later iterations of the app. Missing h1 element: I used a h3 element instead of a h1 element to make styling easier. WAVE is flagging the 'Jot' footer logo link as a redundant link as there is also a link in the nav bar on the same page.|

   
## JavaScript Testing <!-- omit in toc -->
[JSHint Testing](https://jshint.com/) - I ran the JS files through JSHint to make sure it was thoroughly tested, no issues were found.

## Python Testing
[Code Beautifier](https://codebeautify.org/python-formatter-beautifier#) - I ran my python code through this formatter to ensure that it met PEP8 guidlines.

## Known bugs and fixes 
- **Issue:** When connecting MongoDB I initially had issues with it not connecting a specific database.
  - **Solution:** Upon closer inspection, within my env.py file the pre-created Mongo URI link did not contain my specific database name. Once I had added this I was able to test the connection within the command line by adding and removing entries.
- **Issue:** When I had styled the dropdown genre selection to contain white text (in order to contrast with the darker background) I inadvertently targeted all dropdown components including the date picker within my 'Create Entry' and 'Edit Entry' forms. The date picker background was also white which caused the text to be unreadble to the user.
  - **Solution:** Using the 'Inspect' devtool within my browser I was able to directly target various elements of the date picker and change the background to match the rest of the application. I also utilised this when styling other aspects of the form (i.e the 'Would you reccommend?' switch)
- **Issue:** My initial idea for the web application was to create a private journal. I spent a long time trying to find a way to only display the current session users entries to them on a private page that is only viewable when logged in.
  - **Solutions:** In the interests of time constraints and struggling to find answers to my issue I decided to change my idea and create a collaborative book review app that allows all users to edit and delete posts. 

## Testing Credits
- [JShint](https://jshint.com/) - Used for testing JavaScript.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used for testing performance, accessibility, best practices and SEO.
- [Code Beautifier](https://codebeautify.org/python-formatter-beautifier#) - Used to format Python code to PEP8 standards
- [Wave Web Accessiblity Tester](https://wave.webaim.org/) - Used to test accessibility
- 