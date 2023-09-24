export class RegisterElements {
    static get ElementsRegister() {
        return {
            getLoginNavButton: () => cy.get('#login_nav_btn'),
            getRegisterBtnInLoginForm: () => cy.get('#register_from_loginform'),
            getUsernameField: () => cy.get('#registerUsername'),
            getEmailField: () => cy.get('#registerEmail'),
            getPasswordField: () => cy.get('#registerPassword'),
            getConfirmPasswordField: () => cy.get('#registerPasswordRepeat'),
            getRegisterSubmitButton: () => cy.get('#register_button'),
            getBodyText: () => cy.get('body').invoke('text')
        }
    }
}