import { expect, Page, test } from '@playwright/test';
const TODO_URL = 'https://demo.playwright.dev/todomvc/';


test.describe('Grundlegend', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });



    test("Ein neues Todo wird hinzugefügt", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Mein erstes Todo');
        await newTodoInput.press('Enter');

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
    });

    test("Mehrere Todos werden hinzugefügt", async ({ page }: { page: Page }) => {
        await addTodos(page);

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
        await expect(page.getByText('Mein zweites Todo')).toBeVisible();
        await expect(page.getByText('Mein drittes Todo')).toBeVisible();
    });

    test("Checkboxen setzen", async ({ page }: { page: Page }) => {
        await addTodos(page);
        await page.getByRole('listitem').filter({ hasText: 'Mein zweites Todo' }).getByLabel('Toggle Todo').check()

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
        await expect(page.getByText('Mein zweites Todo').locator('..').locator('..')).toHaveClass('completed');
    });

    test("items left prüfen", async ({ page }: { page: Page }) => {
        await addTodos(page);
        await page.getByRole('listitem').filter({ hasText: 'Mein zweites Todo' }).getByLabel('Toggle Todo').check()

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
        await expect(page.getByText('Mein zweites Todo').locator('..').locator('..')).toHaveClass('completed');
        await expect(page.getByText('2 item left')).toBeDefined;
    });
});


//2
test.describe('Löschen & Toggle-All', () => {

    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    test("todo mit X löschen", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await addTodos(page);

        await page.getByText('Mein zweites Todo').hover();
        await page.getByRole('button', { name: 'Delete' }).click();

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
        await expect(page.getByText('2 item left')).toBeDefined;
    });

    test("toggleAll einfach", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await addTodos(page);

        await page.getByText('Mein zweites Todo').hover();
        await page.getByText('Mark all as complete').click();
        await page.getByRole('listitem').filter({ hasText: 'Mein zweites Todo' }).getByLabel('Toggle Todo').check();

        await expect(page.locator('.todo-list .completed')).toHaveCount(3);

        await page.getByText('Mark all as complete').click();

        await expect(page.locator('.todo-list .completed')).toHaveCount(0);

    });

    test("toggleAll mit Vorauswahl", async ({ page }: { page: Page }) => {
        await addTodos(page);
        await page.getByText('Mein zweites Todo').hover();
        await page.getByText('Mark all as complete').click();

        await expect(page.locator('.todo-list .completed')).toHaveCount(3);

        await page.getByText('Mark all as complete').click();

        await expect(page.locator('.todo-list .completed')).toHaveCount(0);

    });

    test("Clear completed", async ({ page }: { page: Page }) => {
        await addTodos(page);
        await page.getByText('Mark all as complete').click();
        await page.getByRole('button', { name: 'Clear completed' }).click();

        await expect(page.locator('.todo-list')).toHaveCount(0);

    });

});

//3
test.describe('Filter', () => {

    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    test("Filte auf active, completed, all", async ({ page }: { page: Page }) => {
        await addTodos(page);
        await page.getByRole('listitem').filter({ hasText: 'Mein erstes Todo' }).getByLabel('Toggle Todo').check();
        await expect(page.locator('.todo-list>li')).toHaveCount(3);
        await expect(page.getByText('3 item left')).toBeDefined;
        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(page.locator('.todo-list>li')).toHaveCount(1);
        await page.getByRole('link', { name: 'Active' }).click();
        await expect(page.locator('.todo-list>li')).toHaveCount(2);
        await expect(page.getByText('1 item left')).toBeDefined;
    });

});

//4
test.describe('Edge Cases', () => {

    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });
    test("edge cases", async ({ page }: { page: Page }) => {
        await expect(page.locator('.todo-list>li')).toHaveCount(0);
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.press('Enter');
        await expect(page.locator('.todo-list>li')).toHaveCount(0);
        await expect(page.getByRole('button', { name: 'Clear completed' })).toBeHidden;
        await expect(page.locator('.todo-list>li')).toHaveCount(0);
        await newTodoInput.fill('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
        await newTodoInput.press('Enter');
        await expect(page.getByText('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')).toBeDefined;
        await expect(page.locator('.todo-list>li')).toHaveCount(1);
    });
});


async function addTodos(page: Page) {
    const newTodoInput = page.getByPlaceholder('What needs to be done?');
    await newTodoInput.fill('Mein erstes Todo');
    await newTodoInput.press('Enter');
    await newTodoInput.fill('Mein zweites Todo');
    await newTodoInput.press('Enter');
    await newTodoInput.fill('Mein drittes Todo');
    await newTodoInput.press('Enter');
}

// TODO: Fügen Sie hier Ihre Tests ein
// Folgen Sie den Anleitungen in der README.md
