import { AddNewProductMethods } from "../pageObjects/products/addNewProduct/addNewProduct.methods";
import { HomeMethods } from "../pageObjects/home/home.methods";
import { LoginMethods } from "../pageObjects/login/login.methods";
import {ProductsMethods} from "../pageObjects/products/products.methods";

  const testData = require('../fixtures/add_new_project.json')

describe('Login Cypress Test', () => {
  let login = new LoginMethods();
  let home = new HomeMethods();
  let products = new ProductsMethods();
  let addNewProduct = new AddNewProductMethods();

  beforeEach(function () {
    home.navigateToHomePage('http://localhost:8000/home/');
    login.navigateToLoginPage();
    login.login("admin", "201107superuser");
    products.navigateToProductPage();
  });

  testData.addNewProjectData.forEach((testcase: {
        name: string;
        price: string;
        image: string;
    }) => {
       it(testcase.name + ' should be able to login', () => {
      products.verifyAddToProductBtnExists();
      products.navigateToAddProductPage();
      addNewProduct.addProduct(testcase.name, testcase.price, testcase.image);
      cy.get('body').invoke('text').should('contain', testcase.name);
    });
  })

});
