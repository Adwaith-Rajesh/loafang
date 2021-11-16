### codes are only for errors

- 600 -> Common Error
- 601 -> Unrecognized method
- 602 -> Unrecognized property key
- 603 -> Missing ID
- 604 -> Invalid Data Type for arguments in the query
- 605 -> Invalid Data Type for the content container for the query
  - eg: Get, Delete, must have a list as its content container
  - eg: All the other methods must have dict as their content container.
- 606 -> Parser does not exists for the given request method
