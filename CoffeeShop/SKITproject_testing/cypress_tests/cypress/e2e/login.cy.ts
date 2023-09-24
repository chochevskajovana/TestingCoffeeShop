import { LoginMethods } from "../pageObjects/login/login.methods";
import {HomeMethods} from "../pageObjects/home/home.methods";

describe('Login Cypress Test', () => {
  let login = new LoginMethods();
  let home = new HomeMethods();
  const testData = require('../fixtures/login.json')

  testData.loginData.forEach((testcase: { username: string; password: string; }) => {
    it(testcase.username + ' should be able to login', () => {
      home.navigateToHomePage('http://localhost:8000/home/');
      login.navigateToLoginPage();
      login.login(testcase.username, testcase.password);
      login.verifyUsernameExistsOnPage(testcase.username);
    })
  });
})