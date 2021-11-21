In this section we will be discussing on what a loafang response looks like. For both an aliased and non aliased queries.

#### Without alias

A sample query


```json
{
    "GET:get-users":{
        "user --name ad":[
            "username",
            "email"
        ],

        "user --name john":[
            "username",
        ]
    },


    "PUT:update-user-john": {
        "user --name john":{
            "username": "john"
        }
    }
}
```

A sample response

```json
{
    "get-users":{
        "user --name ad": {
            "username": "adnyx",
            "email": "adnyx@example.com"
        },

        "user --name john": {
            "username": "johnny"
        }
    },

    "update-user-john":{
        "user --name john"{
            "msg": "Updated Successfully"
        }
    }

}
```


#### Without alias and with a `pe` block.
A sample query

```json
{
    "GET:get-users":{
        "user --name ad":[
            "username",
            "email"
        ],

        "user --name john":[
            "username",
        ]
    },

    "GET:data-john:pe":{
        "user --name john":[
            "username",
            "email"
        ]
    },

    "PUT:update-user-john": {
        "user --name john":{
            "username": "john"
        },

        "after": "data-john"
    }
}
```
A sample response

```json
{
    "get-users":{
        "user --name ad": {
            "username": "adnyx",
            "email": "adnyx@example.com"
        },

        "user --name john": {
            "username": "johnny"
        }
    },

    "update-user-john":{
        "user --name john"{
            "msg": "Updated Successfully"
        },

        "after":{
            "user --name john":{
                "username": "johnny",
                "email": "johnnys@example.com"
            }
        }
    }

}
```

#### With aliases


A sample query


```json
{
    "GET:get-users":{
        "user --name ad | user-ad":[
            "username",
            "email"
        ],

        "user --name john | user-john":[
            "username",
        ]
    },


    "PUT:update-user-john": {
        "user --name john | update-john":{
            "username": "john"
        }
    }
}
```

A sample response

```json
{
    "get-users":{
        "user-ad": {
            "username": "adnyx",
            "email": "adnyx@example.com"
        },

        "user-john": {
            "username": "johnny"
        }
    },

    "update-user-john":{
        "update-john"{
            "msg": "Updated Successfully"
        }
    }

}
```
