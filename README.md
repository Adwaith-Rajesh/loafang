# Loafang

A JSON based RESTapi Query Language. It's mainly for small to intermediate sized project.

## Motivation

- I'm bored.
- I needed a smaller version of graphql.
- It's fun to do something like this

## Why name it Loafang

If you google the synonyms for 'rest' one of the result is 'loaf' or 'loafing'. Now, where do you see the word 'rest', 'REST API' and it more of a language kind of thing so
'loafang' makes sense

## An example Schema

> This is not fixed, but this is what I hope it will look like.

```json
{
	"GET:get-user:pe": {
		"user --name adwaith --age 10": ["username", "email_address"]
	},
	"PUT:up-user": {
		"user --name some-user": {
			"email": "new_email@address.com"
		},
		"after:GET": "get-user"
	}
}
```
