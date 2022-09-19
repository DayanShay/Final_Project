User1_test = "test@check.co.il"
Admin_email = "admin@sela.co.il"
Generic_pass = "12345"
User1_test_Low = "test1@check.co.il"
User2_test_high = "test2@check.co.il"
Valid_pass_low = "1234"
Valid_pass_high = "123456789012345"
Invalid_pass_low = "123"
InValid_pass_high = "1234567890123456"
Validation_error = "One or more validation errors occurred."
Invalid_email_msg = "The Email field is not a valid e-mail address."
No_email_filled_msg = "The Email field is required."
Invalid_password_msg = "Your password is limited to 4 to 15 characters"
No_password_filled_msg = "The Password field is required."
Invalid_msg = (Validation_error, Invalid_email_msg, No_email_filled_msg, Invalid_password_msg, No_password_filled_msg)
must_be_signed = "Must be signed in to purchase."
Unauthorized_msg = 'Unauthorized'
no_ammount_in_stoke = 'AxiosError: Request failed with status code 400'
perchuse_error_api = 'Bad Request'
Dup_account = {
  "DuplicateUserName": [
    "Username 'usasdasdasder@example.com' is already taken."
  ]
}

HEADERS = {'accept': 'application/json'}





USER_no_email_and_no_pass = {
    "email": "",
    "password": "",
    "firstName": "string",
    "lastName": "string"
}
USER_invalid_email_and_no_pass = {
    "email": "asadasda.asdasd.asdasd",
    "password": "",
    "firstName": "string",
    "lastName": "string"
}
USER_invalid_email_with_pass = {
    "email": "asadasda.asdasd.asdasd",
    "password": Generic_pass,
    "firstName": "string",
    "lastName": "string"
}
USER_noemail_Generic_pass = {
    "email": "",
    "password": Generic_pass,
    "firstName": "string",
    "lastName": "string"
}
USER_noemail_invalid_low_password = {
    "email": "",
    "password": Invalid_pass_low,
    "firstName": "string",
    "lastName": "string"
}
USER_noemail_invalid_high_password = {
    "email": "",
    "password": InValid_pass_high,
    "firstName": "string",
    "lastName": "string"
}
USER_withemail_invalid_low_password = {
    "email": User1_test,
    "password": Invalid_pass_low,
    "firstName": "string",
    "lastName": "string"
}
USER_withemail_invalid_high_password = {
    "email": User1_test,
    "password": InValid_pass_high,
    "firstName": "string",
    "lastName": "string"
}
USER_Admin_noepass = {
    "email": Admin_email,
    "password": "",
    "firstName": "string",
    "lastName": "string"
}
USER_testuser_noepass = {
    "email": "test@cheack.co.il",
    "password": "",
    "firstName": "string",
    "lastName": "string"
}
USER_testuser = {
    "email": "test@cheack.co.il",
    "password": Generic_pass,
    "firstName": "string",
    "lastName": "string"
}

USER_Admin ={
    "email": Admin_email,
    "password": Generic_pass,
    "firstName": "string",
    "lastName": "string"
}

USER_Login = {
    "email": USER_no_email_and_no_pass["email"],
    "password": USER_no_email_and_no_pass["password"]
}

Create_Author_Dto_test = {
    "name": "Sela Inc",
    "homeLatitude": 32.09720633857184,
    "homeLongitude": 34.82631068248099
}
Update_Author_Dto_test = {
    "name": "Moshe",
    "homeLatitude": 0,
    "homeLongitude": 0,
    "id": 1
}
Create_Book_Dto_test = {
    "name": "Qa & Automation testing",
    "description": "Learn how to Become Qa & Automation Engineer , Step by Step.",
    "price": 1200,
    "amountInStock": 15,
    "imageUrl": "https://www.zibtek.com/blog/content/images/size/w2000/2020/03/Yellow-Modern-Creative-Corporate-Social-Media-Strategy-Presentation--13--2.png",
    "authorId": 0
}
