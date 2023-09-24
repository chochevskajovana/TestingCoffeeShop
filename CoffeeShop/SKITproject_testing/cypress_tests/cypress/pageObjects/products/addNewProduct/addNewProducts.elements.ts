export class AddNewProductsElements {
    static get ElementsAddNewProducts() {
        return {
            getNameField: () => cy.get('#add_new_product_name'),
            getPriceField: () => cy.get('#add_new_product_price'),
            getImageField: () => cy.get('#add_new_product_image'),
            getAddProductSubmitButton: () => cy.get('#add_new_product_submit'),
            getBodyText: () => cy.get('body').invoke('text')
        }
    }
}


