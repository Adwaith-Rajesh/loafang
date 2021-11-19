# Loafang

[![GitHub](https://img.shields.io/github/license/Adwaith-Rajesh/loafang?style=for-the-badge)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/loafang?color=light&style=for-the-badge)](https://pypi.org/project/loafang/)
[![Azure DevOps builds (branch)](https://img.shields.io/azure-devops/build/adwaithrajesh/8d11fcc8-9bf7-41cf-95af-bd240456c13e/9/master?label=azure%20pipelines&style=for-the-badge)](https://dev.azure.com/adwaithrajesh/adwaith/_build?definitionId=9)

A JSON based RESTapi Query Language. It's mainly for small to intermediate sized project.

## Motivation

- I'm bored.
- I needed a smaller version of graphql.
- It's fun to do something like this

## Why name it Loafang

If you google the synonyms for 'rest' one of the result is 'loaf' or 'loafing'. Now, where do you see the word 'rest', 'REST API' and it more of a language kind of thing so
'loafang' makes sense

## An example Schema

```json
{
	"GET:get-user:pe": {
		"user --name adwaith --age 10": ["username", "email_address"]
	},
	"PUT:up-user": {
		"user --name some-user": {
			"email": "new_email@address.com"
		},
		"after": "get-user"
	}
}
```

For more docs visit: [https://adwaith-rajesh.github.io/loafang/](https://adwaith-rajesh.github.io/loafang/)

## Road Map

- [x] Things kind of works
- [x] Make an easier API for the user to use.
- [ ] More tests
