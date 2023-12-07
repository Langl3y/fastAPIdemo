from fastapi import status, HTTPException


class APIResponseMessage(object):
    SUCCESSFULLY_CREATED = {
        "status_code": status.HTTP_201_CREATED,
        "message": "Student created successfully",
        "data": None
    }

    SUCCESSFULLY_RETRIEVED = {
        "status_code": status.HTTP_200_OK,
        "message": "Students retrieved successfully",
        "data": None
    }

    SUCCESSFULLY_UPDATED = {
        "status_code": status.HTTP_200_OK,
        "message": "Students updated successfully",
        "data": None
    }

    SUCCESSFULLY_DELETED = {
        "status_code": status.HTTP_200_OK,
        "message": "Students deleted successfully",
    }

    FAILED_TO_CREATE = {
        "status_code": status.HTTP_409_CONFLICT,
        "message": "Student could not be created",
    }

    FAILED_TO_RETRIEVE = {
        "status_code": status.HTTP_204_NO_CONTENT,
        "message": "No student found",
    }



