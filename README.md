# Flask-Blog

[Flask Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1)

## Routes

**Main:**

	`/home`

	`/about`

**Users:**

	`/register`

	`/login`

	`/logout`

	`/account`

	`/user/:username`

	`/reset_password`

**Posts:**

	`/post/new`

	`/post/:id`

	`//post/:id/update`

	`/post/:id/delete`

### A typical top-level directory layout
    .
    ├── flaskblog
	|	├── errors
	|	├── main
	|	├── posts
	|	├── static
	|	├── templates
	|	├── users
    ├── .env.sample
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    └── run.py
