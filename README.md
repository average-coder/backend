
# Average Coders Backend

This project is the backend for the average coders website. It is built using the Django-rest-framework.

---

### API ENDPOINTS

| NAME | LINK | Authentication Required | Method |
| --- | --- | --- | --- |
| List all posts | /list/ | No | GET |
| Search for specific post | /list/?search=[search_string]/ | No | GET |
| Get post | /post/[slug]/ | No | GET |
| Request a post | /post-request/ | No | POST |
| Add a comment | /comment/ | No | POST |
| Add a sub comment | /sub-comment/ | No | POST |
| Suggestions | /suggestions/ | No | GET |
| Login | /auth/login/ | No | POST |
| Logout | /auth/logout/ | Yes | POST |
| User details | /user/ | Yes | GET |
| Editor | /editor/ | Yes | ALL |
| List posts or editor | /editor-list/ | Yes | GET |
| Image Uploader | /image/ | Yes | POST, GET, DELETE|

---

### BACKEND LINK
[Average Coder Backend](https://avgcdr.tk/api/)

