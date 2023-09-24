import {LoginElements} from "../login/login.elements";

export class HomeMethods{
    navigateToHomePage(page: string) {
        cy.visit(page);
    }
    navigateToCertainPage(page: string){
        cy.visit(page);
    }
}