export class CheckoutElements {
    static get ElementsCheckout() {
        return {
            getCartCheckoutButton: () => cy.get('#cart_checkout_btn'),
            getNameField: () => cy.get('#name'),
            getAddressField: () => cy.get('#address'),
            getPhoneField: () => cy.get('#phone'),
            getDoneCheckoutButton: () => cy.get('#doneCheckout'),
        }
    }
}


