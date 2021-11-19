## <span style="color:#33B864">A sample query</span>

This is what a sample **loafang** query looks like

```json
{
    "GET:get-users":{
        "user --name ad":[
            "username",
            "email"
        ],

        "user --name john":[
            "username",
            "email"
        ]
    },

    "GET:get-user-fred:pe": {
        "user --name fred":[
            "username",
            "email"
        ]
    },

    "PUT:update-user-fred": {
        "user --name fred":{
            "username": "fredmy"
        },

        "after": "get-user-fred"
    }
}
```

## <span style="color:#33B864">The execution block.</span>

```json
"GET:get-users":{
        "user --name ad":[
            "username",
            "email"
        ],

        "user --name john":[
            "username",
            "email"
        ]
    },
```

This is what's called as a Execution block. And a loafang query is made by stacking together a bunch of these Execution Blocks.


### <span style="color:#33B864">Parts of an execution block</span>

#### <span style="color:#FF134B">The header</span>

```json
GET:get-users
```

This is the header of an execution block and is made up of three parts.

 - The request type. (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`)

 - A unique identification string for the execution block

 - And a block property key(Optional)

 The three parts are arranged in the following order


 **`METHOD:ID:PROPERTY_KEY`**

 The ID must be unique among all the execution blocks in a given `loafang` query.

 A property key can completely change the behavior of an execution block.

 Currently there is only one property key that is `pe`. The `pe` key will skip the execution of the given block

#### <span style="color:#FF134B">The Body</span>

The body of an execution block is made up of all the queries that needs to be executed.
The request methods (`GET`, `POST`, ...) of each query will be the one specified in the header of the execution block.

##### Parts of a query.

The query has two parts, the args (the head and parameters) and the content of the query.

```json
 "user --name john": [
            "username",
            "email"
        ]
```

This is a sample query inside an execution block.

Here,

`user` if the head of the query or where the query the query need to executed, this can be a database name or anything like that.

`--name john` is the parameter to the query. These can be parameter to filter the head.

`["username", "email"]` These are the content of the query, these can be the fields that you wish to get from the database with the specified parameters.

The contents of the query must be a list for `GET` and `DELETE` queries and must be a `dict` / `JSON object` for `PUT`, `POST`, and `PATCH`.


##### The after key.

The `after` key in an execution block species another execution block that needs to executed after the current block has done executing. This can be used to retrieve data after a `POST` request has been made.

 - The after key can only point to an execution block that has `pe` as it's property key.

 - An execution block that has `pe` as it's property key cannot have an after key.
