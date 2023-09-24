import {RegisterMethods} from "../pageObjects/register/register.methods";
import {LoginMethods} from "../pageObjects/login/login.methods";
import {HomeMethods} from "../pageObjects/home/home.methods";

describe('Register Cypress test', () => {
    let login = new LoginMethods();
    let register = new RegisterMethods()
    let home = new HomeMethods()
    const testDataLogin = require('../fixtures/login_after_register.json')
    const testDataRegister = require('../fixtures/register.json')

    beforeEach(function () {
        home.navigateToHomePage('http://localhost:8000/home/');
        login.navigateToLoginPage();
    })

    // Trying to log in when the user is not register (Should not be able to login)
    testDataLogin.loginAfterRegisterData.forEach((testcase: { username: string; password: string; }) => {
        it(testcase.username + ' should not be able to login', () => {
            login.login(testcase.username, testcase.password);
            login.verifyUsernameDoesNotExistsOnPage(testcase.username);
        })
    });

    // The user is registering
    testDataRegister.registerData.forEach((testcase: {
        username: string;
        email: string;
        password: string;
        repeat_password: string
    }) => {
        it(testcase.username + ' should be able to register', () => {
            register.navigateToRegisterPage();
            register.register(testcase.username, testcase.email, testcase.password, testcase.repeat_password);
        })
    });

    // The user is logging in
    testDataLogin.loginAfterRegisterData.forEach((testcase: { username: string; password: string; }) => {
        it(testcase.username + ' should be able to login', () => {
            login.login(testcase.username, testcase.password);
            login.verifyUsernameExistsOnPage(testcase.username);
        })
    });
})