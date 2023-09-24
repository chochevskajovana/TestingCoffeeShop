import { HomeMethods } from "../pageObjects/home/home.methods";
import { LoginMethods } from "../pageObjects/login/login.methods";
import {ProductsMethods} from "../pageObjects/products/products.methods";
// import { AddNewProductMethods } from "../pageObjects/products/addNewProduct/addNewProduct.methods";
// import {EditProductMethods} from "../pageObjects/products/editProduct/editProduct.methods";

const testData = require('../fixtures/add_new_project.json')

describe('Login Cypress Test', () => {
  let login = new LoginMethods();
  let home = new HomeMethods();
  let products = new ProductsMethods();
  // let addNewProduct = new AddNewProductMethods();
  // let editProduct = new EditProductMethods();

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
      products.navigateToNextProductPage();
      products.verifyDeleteProductBtnExists();
      products.navigateToNextProductPage();
      cy.get('body').invoke('text').should('not.contain', testcase.name);
    });
  })

});
