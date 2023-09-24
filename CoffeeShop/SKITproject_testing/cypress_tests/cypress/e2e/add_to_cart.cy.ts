import { HomeMethods } from "../pageObjects/home/home.methods";
import { LoginMethods } from "../pageObjects/login/login.methods";
import {ProductsMethods} from "../pageObjects/products/products.methods";

  const testData = require('../fixtures/add_project_to_cart.json')

describe('Login Cypress Test', () => {
  let login = new LoginMethods();
  let home = new HomeMethods();
  let products = new ProductsMethods();

  beforeEach(function () {
    home.navigateToHomePage('http://localhost:8000/home/');
    login.navigateToLoginPage();
    login.login("admin", "201107superuser");
    products.navigateToProductPage();
  });

  testData.addProjectToCartData.forEach((testcase: {
        name: string;
        price: string;
        image: string;
    }) => {
       it(testcase.name + ' should be able to login', () => {
       products.verifyAddProductToCartBtnExists();
       products.navigateToCartPage();
      cy.get('body').invoke('text').should('contain', testcase.name);
    });
  })

});
