"""
test_create_template
--------------------
"""

def test_pre_prompt_exit(cookies, capfd):
    result = cookies.bake()
    captured = capfd.readouterr()
    assert "The napari cookiecutter plugin template has been replaced with a copier template!" in captured.out
    assert "For more information, refer to the template README:" in captured.out
    assert "https://github.com/napari/napari-plugin-template" in captured.out
    assert result.exit_code == -1
    assert str(result.exception) == 'Pre-Prompt Hook script failed'
