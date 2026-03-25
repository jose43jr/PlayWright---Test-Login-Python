import pytest

def test_login_sem_dados(page):
    # Acessa a aplicação
    page.goto("https://www.saucedemo.com/")

    # Ação: tenta logar sem preencher
    page.click('[data-test="login-button"]')

    # Validação: erro deve aparecer
    erro = page.locator('[data-test="error"]')

    assert erro.is_visible(), "Erro não exibido para login sem dados"
    assert "Username is required" in erro.inner_text()