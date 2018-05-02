import { LoginRequest } from LoginModel

export class LoginPresenter {
    constructor() {

    }
    initializeView() {

        document.querySelector("#input_email").focus();
        document.querySelector("#input_email").onkeyup = function (e) {
            if (e.keyCode === Constants.RETURN_KEYSTROKE) {
                document.querySelector("#button_login").click();
            }
        };
        document.querySelector("#input_password").focus();
        document.querySelector("#input_password").onkeyup = function (e) {
            if (e.keyCode === Constants.RETURN_KEYSTROKE) {
                document.querySelector("#button_login").click();
            }
        };

       /* document.querySelector("#button_login").onclick = function (e) {
            var email = document.querySelector("#input_email");
            var password = document.querySelector("#input_password");
            $.ajax({
                url: 'login',
                data: {
                    'email': email,
                    'password': password
                },
                dataType: 'json',
                success: function(data){
                    alert('success!');
                },
                failure: function(data){
                    alert('failure...');
                },
            });
        };

        document.querySelector("#button_register").onclick = function (e) {
            window.location.pathname = '/register';
        }*/
    }
}