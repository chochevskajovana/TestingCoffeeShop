export class ProductsElements{
    static get ElementsProducts(){
        return{
            getProductsNavButton: () => cy.get('#products_nav_btn'),
            getCartNavButton: () => cy.get('#cart_nav_btn'),
            getAddNewProductsButton: () => cy.get('#add_new_product'),
            getNextProductPageButton: () => cy.get('#next_product_page'),
            getEditProductButton: () => cy.get(".editProject"),
            getDeleteProductButton: () => cy.get(".deleteProject"),
            getAddToCart: () => cy.get(".addProductToCart"),
        }
    }
}