export class LoginElements {
    static get ElementsLogin() {
        return {
            getLoginNavButton: () => cy.get('#login_nav_btn'),
            getUsernameField: () => cy.get('#inputUsername'),
            getPasswordField: () => cy.get('#inputPassword'),
            getLoginSubmitButton: () => cy.get('#login_button'),
            getBodyText: () => cy.get('body').invoke('text')
        }
    }
}


