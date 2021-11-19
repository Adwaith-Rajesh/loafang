METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE"
]

PROPERTY_KEYS = [
    "pe"
]

ERROR_CODES = {
    600: "Something went wrong.",
    601: "The header cannot be empty.",
    602: "Unrecognized method.",
    603: "Unrecognized property key.",
    604: "Missing ID.",
    605: "Invalid data type for the argument in the query.",
    606: "Invalid Data Type for the content container for the query.",
    607: "Parser does not exists for the given request method.",
    608: "Two Execution Blocks cannot have the same ID's.",
    609: "The after key must be a string",
    610: "The Execution block with the given ID does not exists",
    611: "Methods is not implemented",
    612: "Execution block with pe property key cannot have an after key"

}
