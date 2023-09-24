import {AddNewProductsElements} from "../addNewProduct/addNewProducts.elements";
import {ProductsElements} from "../products.elements";
import {EditProductsElements} from "./editProducts.elements";

export class EditProductMethods{
    editProduct(name, price, image) {
    EditProductsElements.ElementsEditProducts.getNameField().type(name);
    EditProductsElements.ElementsEditProducts.getPriceField().type(price);
    EditProductsElements.ElementsEditProducts.getImageField();

    EditProductsElements.ElementsEditProducts.getAddProductSubmitButton().click();
    ProductsElements.ElementsProducts.getNextProductPageButton().click();
}
}