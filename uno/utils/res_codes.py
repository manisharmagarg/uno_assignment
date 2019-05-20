from copy import copy


STATUS = "status"
STATUS_CODE = "code"
MESSAGE = "msg"
DATA = 'data'

INVALID_POST_DATA = "1000"
NO_ACCESS = "1001"
NOT_FOUND = "1002"
LOGIN_SUCCESS = "1003"
WRONG_PASSWORD_ENTERED = "1004"
PASSWORD_UPDATE_SUCCESS = "1005"
USER_PROFILE_UPDATED = "1006"

SUCCESS = "2000"
COURSE_CREATED = "3000"
COURSE_UPDATED = "3001"
COURSE_DELETED = "3002"
COURSE_DETAIL = "3003"
COURSE_SECTION_CREATED = "3004"
COURSE_SECTION_UPDATED = "3005"
COURSE_SECTION_DELETED = "3006"
COURSE_SECTION_FILE_CREATED = "3007"
COURSE_SECTION_FILE_UPDATED = "3008"
COURSE_SECTION_FILE_DELETED = "3009"
COURSE_DETAIL_TAB_CREATED = "3010"
COURSE_DETAIL_TAB_UPDATED = "3011"
COURSE_DETAIL_TAB_DELETED = "3012"
COURSE_DETAIL_TAB_LIST_CREATED = "3013"
COURSE_DETAIL_TAB_LIST_UPDATED = "3014"
COURSE_DETAIL_TAB_LIST_DELETED = "3015"
COURSE_NOT_FOUND_FOR_USER = "3016"
USER_ADDED_COURSE = "3017"
USER_DELETED_COURSE = "3018"
ASSIGNMENT_CREATED = "5000"
ASSIGNMENT_UPDATED = "5001"
ASSIGNMENT_DELETED = "5002"
ASSIGNMENT_FILE_CREATED = "5003"
ASSIGNMENT_FILE_UPDATED = "5004"
ASSIGNMENT_FILE_DELETED = "5005"
ASSIGNMENT_SOLUTION_CREATED = "5006"
ASSIGNMENT_SOLUTION_FILE_UPLOADED = "5007"
CATEGORY_CREATED = "6000"
CATEGORY_UPDATED = "6001"
CATEGORY_DELETED = "6002"
CATEGORY_COURSE_CREATED = "6003"
CATEGORY_COURSE_UPDATED = "6004"
CATEGORY_COURSE_DELETED = "6005"
PK_NOT_FOUND = "4000"

"""
#######################################################
#################### ACCOUNT ##########################
#######################################################
"""

SIGNUP_SUCCESS = "2001"

############################################################################

RESPONSE_LOOKUP = {
    INVALID_POST_DATA: {
        STATUS_CODE: int(INVALID_POST_DATA),
        MESSAGE: "Invalid post data provided"
    },
    NO_ACCESS: {
        STATUS_CODE: int(NO_ACCESS),
        MESSAGE: "You don't have authorization access to use this page"
    },
    NOT_FOUND: {
        STATUS_CODE: int(NOT_FOUND),
        MESSAGE: "Requested entity not found"
    },
    LOGIN_SUCCESS: {
        STATUS_CODE: int(LOGIN_SUCCESS),
        MESSAGE: "Login authentication is successful"
    },


    SUCCESS: {
        STATUS_CODE: int(SUCCESS),
        MESSAGE: "Request processed successfully"
    },
    PK_NOT_FOUND: {
        STATUS_CODE: int(PK_NOT_FOUND),
        MESSAGE: "Such pk not found"
    },
    # account
    SIGNUP_SUCCESS: {
        STATUS_CODE: int(SIGNUP_SUCCESS),
        MESSAGE: "Login your register email and varify your Account"
    },
    WRONG_PASSWORD_ENTERED: {
        STATUS_CODE: int(WRONG_PASSWORD_ENTERED),
        MESSAGE: "Wrong password supplied."
    },
    PASSWORD_UPDATE_SUCCESS: {
        STATUS_CODE: int(PASSWORD_UPDATE_SUCCESS),
        MESSAGE: "Password updated successfully."
    },
    USER_PROFILE_UPDATED: {
        STATUS_CODE: int(USER_PROFILE_UPDATED),
        MESSAGE: "User detail updated successfully."
    },
    #course
    COURSE_CREATED: {
        STATUS_CODE: int(COURSE_CREATED),
        MESSAGE: "Course created successfully"
    },
    COURSE_UPDATED: {
        STATUS_CODE: int(COURSE_UPDATED),
        MESSAGE: "Course updated successfully"
    },
    COURSE_DELETED: {
        STATUS_CODE: int(COURSE_DELETED),
        MESSAGE: "Course deleted successfully"
    },
    COURSE_NOT_FOUND_FOR_USER: {
        STATUS_CODE: int(COURSE_NOT_FOUND_FOR_USER),
        MESSAGE: "Course Not found for this user"
    },
    USER_ADDED_COURSE: {
        STATUS_CODE: int(USER_ADDED_COURSE),
        MESSAGE: "Course added to library successfully"
    },
    USER_DELETED_COURSE: {
        STATUS_CODE: int(USER_DELETED_COURSE),
        MESSAGE: "Course removed successfully from library"
    },
    #Course section
    COURSE_SECTION_CREATED: {
        STATUS_CODE: int(COURSE_SECTION_CREATED),
        MESSAGE: "Course Section created successfully"
    },
    COURSE_SECTION_UPDATED: {
        STATUS_CODE: int(COURSE_SECTION_UPDATED),
        MESSAGE: "Course Section updated successfully"
    },
    COURSE_SECTION_DELETED: {
        STATUS_CODE: int(COURSE_SECTION_DELETED),
        MESSAGE: "Course Section deleted successfully"
    },
    #Course file
    COURSE_SECTION_FILE_CREATED: {
        STATUS_CODE: int(COURSE_SECTION_FILE_CREATED),
        MESSAGE: "Course Section File saved successfully"
    },
    COURSE_SECTION_FILE_UPDATED: {
        STATUS_CODE: int(COURSE_SECTION_FILE_UPDATED),
        MESSAGE: "Course Section File updated successfully"
    },
    COURSE_SECTION_FILE_DELETED: {
        STATUS_CODE: int(COURSE_SECTION_FILE_DELETED),
        MESSAGE: "Course Section File deleted successfully"
    },
    # Course Detail Tab
     COURSE_DETAIL_TAB_CREATED: {
        STATUS_CODE: int(COURSE_DETAIL_TAB_CREATED),
        MESSAGE: "Course Detail Tab created successfully"
    },
    COURSE_DETAIL_TAB_UPDATED: {
        STATUS_CODE: int(COURSE_DETAIL_TAB_UPDATED),
        MESSAGE: "Course Detail Tab updated successfully"
    },
    COURSE_DETAIL_TAB_DELETED: {
        STATUS_CODE: int(COURSE_DETAIL_TAB_DELETED),
        MESSAGE: "Course Detail Tab deleted successfully"
    },
    # Course Detail Tab List
    COURSE_DETAIL_TAB_LIST_CREATED: {
        STATUS_CODE: int(COURSE_DETAIL_TAB_LIST_CREATED),
        MESSAGE: "Course Detail Tab List created successfully"
    },
    COURSE_DETAIL_TAB_LIST_UPDATED: {
        STATUS_CODE: int(COURSE_DETAIL_TAB_LIST_UPDATED),
        MESSAGE: "Course Detail Tab List updated successfully"
    },
    COURSE_DETAIL_TAB_LIST_DELETED: {
        STATUS_CODE: int(COURSE_DETAIL_TAB_LIST_DELETED),
        MESSAGE: "Course Detail Tab List deleted successfully"
    },
    # Assignment
    ASSIGNMENT_CREATED: {
        STATUS_CODE: int(ASSIGNMENT_CREATED),
        MESSAGE: "Assignment created successfully"
    },
    ASSIGNMENT_UPDATED: {
        STATUS_CODE: int(ASSIGNMENT_UPDATED),
        MESSAGE: "Assignment updated successfully"
    },
    ASSIGNMENT_DELETED: {
        STATUS_CODE: int(ASSIGNMENT_DELETED),
        MESSAGE: "Assignment deleted successfully"
    },
    # Assignment File
    ASSIGNMENT_FILE_CREATED: {
        STATUS_CODE: int(ASSIGNMENT_FILE_CREATED),
        MESSAGE: "Assignment File saved successfully"
    },
    ASSIGNMENT_FILE_UPDATED: {
        STATUS_CODE: int(ASSIGNMENT_FILE_UPDATED),
        MESSAGE: "Assignment File updated successfully"
    },
    ASSIGNMENT_FILE_DELETED: {
        STATUS_CODE: int(ASSIGNMENT_FILE_DELETED),
        MESSAGE: "Assignment File deleted successfully"
    },
    # Assignment File
    ASSIGNMENT_SOLUTION_CREATED: {
        STATUS_CODE: int(ASSIGNMENT_SOLUTION_CREATED),
        MESSAGE: "Assignment Solution Created successfully"
    },
    # Assignment Solution File
    ASSIGNMENT_SOLUTION_FILE_UPLOADED: {
        STATUS_CODE: int(ASSIGNMENT_SOLUTION_FILE_UPLOADED),
        MESSAGE: "Assignment Solution File Uploaded successfully"
    },
    # category
    CATEGORY_CREATED: {
        STATUS_CODE: int(CATEGORY_CREATED),
        MESSAGE: "Category created successfully"
    },
    CATEGORY_UPDATED: {
        STATUS_CODE: int(CATEGORY_UPDATED),
        MESSAGE: "Category updated successfully"
    },
    CATEGORY_DELETED: {
        STATUS_CODE: int(CATEGORY_DELETED),
        MESSAGE: "Category deleted successfully"
    },
    # category course
    CATEGORY_COURSE_CREATED: {
        STATUS_CODE: int(CATEGORY_COURSE_CREATED),
        MESSAGE: "Category course created successfully"
    },
    CATEGORY_COURSE_UPDATED: {
        STATUS_CODE: int(CATEGORY_COURSE_UPDATED),
        MESSAGE: "Category course updated successfully"
    },
    CATEGORY_COURSE_DELETED: {
        STATUS_CODE: int(CATEGORY_COURSE_DELETED),
        MESSAGE: "Category course deleted successfully"
    },

}


def get_response_dict(lookup, data=None, substitute=None):
    response_data = copy(RESPONSE_LOOKUP.get(lookup, {
        STATUS_CODE: 0,
        MESSAGE: "Something Went Wrong",
        DATA: ''
    }))
    if data is not None:
        response_data[DATA] = data
    if substitute:
        response_data[MESSAGE] = response_data[MESSAGE] % substitute
    return response_data

