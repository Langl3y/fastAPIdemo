from fastapi import status


class APIResponseMessage:
    SUCCESSFULLY_CREATED = {
        "status_code": status.HTTP_201_CREATED,
        "message": "created successfully",
        "data": None
    }

    SUCCESSFULLY_RETRIEVED = {
        "status_code": status.HTTP_200_OK,
        "message": "retrieved successfully",
        "data": None
    }

    SUCCESSFULLY_UPDATED = {
        "status_code": status.HTTP_200_OK,
        "message": "updated successfully",
        "data": None
    }

    SUCCESSFULLY_DELETED = {
        "status_code": status.HTTP_200_OK,
        "message": "deleted successfully",
    }

    FAILED_TO_CREATE = {
        "status_code": status.HTTP_409_CONFLICT,
        "message": "could not be created",
    }

    FAILED_TO_RETRIEVE = {
        "status_code": status.HTTP_204_NO_CONTENT,
        "message": "Not found",
    }



