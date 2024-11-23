const PORT = process.env.PORT || 5500;

describe('BMI Calculator', function () {
    it('successfully loads', function () {
        cy.visit(`http://localhost:${PORT}`) // ändern Sie URL zu Ihrer App
    })

    it('has the correct title', function () {
        cy.visit(`http://localhost:${PORT}`) // ändern Sie URL zu Ihrer App
        cy.title().should('include', 'BMI Rechner')
    });

    it('has the correct heading', function () {
        cy.visit(`http://localhost:${PORT}`) // ändern Sie URL zu Ihrer App
        cy.get('h1').should('contain', 'BMI Rechner')
    });

    it('shows the correct BMI value', function () {
        cy.visit(`http://localhost:${PORT}`) // ändern Sie URL zu Ihrer App
        cy.get('#weight').as('range').invoke('val', 76).trigger('change')
        cy.get('#height').as('range').invoke('val', 181).trigger('change')
        cy.get('#bmi').should('contain', '23.2')
    })
})
