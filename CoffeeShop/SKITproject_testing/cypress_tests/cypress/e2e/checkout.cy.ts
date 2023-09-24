import { HomeMethods } from "../pageObjects/home/home.methods";
import { LoginMethods } from "../pageObjects/login/login.methods";
import {ProductsMethods} from "../pageObjects/products/products.methods";
import {CheckoutMethods} from "../pageObjects/cart/checkout/checkout.methods";

  const testData = require('../fixtures/checkout.json')

describe('Login Cypress Test', () => {
  let login = new LoginMethods();
  let home = new HomeMethods();
  let products = new ProductsMethods();
  let checkout = new CheckoutMethods();

  beforeEach(function () {
    home.navigateToHomePage('http://localhost:8000/home/');
    login.navigateToLoginPage();
    login.login("admin", "201107superuser");
    products.navigateToProductPage();
  });

  testData.CheckoutData.forEach((testcase: {
        name: string;
        address: string;
        phone: string;
    }) => {
       it(testcase.name + ' should be able to login', () => {
       checkout.verifyAddProductToCartForCheckoutBtnExists();
       products.navigateToCartPage();
       checkout.verifyCheckoutBtnExists();
       checkout.addCheckoutInfo(testcase.name, testcase.address, testcase.phone);
      cy.get('body').invoke('text').should('contain', "Your order has been successfully sent");

    });
  })
});