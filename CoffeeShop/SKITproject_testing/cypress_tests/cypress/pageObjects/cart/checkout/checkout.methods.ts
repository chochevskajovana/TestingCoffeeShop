import {CheckoutElements} from "./checkout.elements";
import {ProductsElements} from "../../products/products.elements";

export class CheckoutMethods {
     verifyCheckoutBtnExists(){
        CheckoutElements.ElementsCheckout.getCartCheckoutButton().should("exist").click();
    }

    addCheckoutInfo(name, address, phone){
        CheckoutElements.ElementsCheckout.getNameField().type(name)
        CheckoutElements.ElementsCheckout.getAddressField().type(address)
        CheckoutElements.ElementsCheckout.getPhoneField().type(phone)
        CheckoutElements.ElementsCheckout.getDoneCheckoutButton().click()
    }

    verifyAddProductToCartForCheckoutBtnExists(){
        ProductsElements.ElementsProducts.getAddToCart().eq(1).should("exist").click();
    }
}