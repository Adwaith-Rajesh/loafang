### codes are only for errors

- 600 -> Something went Wrong
- 601 -> The header cannot be empty
- 602 -> Unrecognized method
- 603 -> Unrecognized property key
- 604 -> Missing ID
- 605 -> Invalid Data Type for arguments in the query
- 606 -> Invalid Data Type for the content container for the query
  - eg: Get, Delete, must have a list as its content container
  - eg: All the other methods must have dict as their content container.
- 607 -> Parser does not exists for the given request method
- 608 -> Two Execution Blocks cannot have the same ID's
- 609 -> The after key must be a string
- 610 -> The Execution block with the given ID does not exists
- 611 -> Methods is not implemented
