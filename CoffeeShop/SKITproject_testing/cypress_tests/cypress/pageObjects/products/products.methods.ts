import {ProductsElements} from "./products.elements"

export class ProductsMethods{

    navigateToProductPage(){
        ProductsElements.ElementsProducts.getProductsNavButton().click()
    }
    navigateToNextProductPage(){
        ProductsElements.ElementsProducts.getNextProductPageButton().click()
    }

    navigateToCartPage(){
        ProductsElements.ElementsProducts.getCartNavButton().click()
    }

    verifyAddToProductBtnExists(){
        ProductsElements.ElementsProducts.getAddNewProductsButton().should("exist");
    }

    navigateToAddProductPage(){
        ProductsElements.ElementsProducts.getAddNewProductsButton().click()
    }

    verifyEditProductBtnExists(){
        ProductsElements.ElementsProducts.getEditProductButton().eq(1).should("exist").click();
    }

    verifyDeleteProductBtnExists(){
        ProductsElements.ElementsProducts.getDeleteProductButton().eq(1).should("exist").click();
    }

    verifyAddProductToCartBtnExists(){
        ProductsElements.ElementsProducts.getAddToCart().eq(0).should("exist").click();
    }
}
