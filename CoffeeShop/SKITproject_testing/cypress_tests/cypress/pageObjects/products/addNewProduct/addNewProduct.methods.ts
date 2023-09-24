import {AddNewProductsElements} from "./addNewProducts.elements";
import {ProductsElements} from "../products.elements";

export class AddNewProductMethods{

   addProduct(name, price, image) {
    AddNewProductsElements.ElementsAddNewProducts.getNameField().type(name);
    AddNewProductsElements.ElementsAddNewProducts.getPriceField().type(price);
    AddNewProductsElements.ElementsAddNewProducts.getImageField();

    AddNewProductsElements.ElementsAddNewProducts.getAddProductSubmitButton().click();
    ProductsElements.ElementsProducts.getNextProductPageButton().click();
}

}