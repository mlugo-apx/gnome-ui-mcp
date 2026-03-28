"""Tests for mcp API surface compatibility.

Guards against breakage when the mcp dependency constraint is loosened.
Every import and constructor pattern used in server.py is verified here.
"""

from __future__ import annotations


class TestMcpImports:
    def test_fastmcp_importable(self) -> None:
        from mcp.server.fastmcp import FastMCP

        assert callable(FastMCP)

    def test_calltoolresult_importable(self) -> None:
        from mcp.types import CallToolResult

        assert callable(CallToolResult)

    def test_textcontent_importable(self) -> None:
        from mcp.types import TextContent

        assert callable(TextContent)


class TestMcpConstruction:
    def test_fastmcp_constructor(self) -> None:
        from mcp.server.fastmcp import FastMCP

        instance = FastMCP(name="test-server", instructions="test instructions")
        assert instance.name == "test-server"

    def test_fastmcp_has_tool_decorator(self) -> None:
        from mcp.server.fastmcp import FastMCP

        instance = FastMCP(name="test-server", instructions="test")
        assert hasattr(instance, "tool") and callable(instance.tool)

    def test_fastmcp_has_run_method(self) -> None:
        from mcp.server.fastmcp import FastMCP

        instance = FastMCP(name="test-server", instructions="test")
        assert hasattr(instance, "run") and callable(instance.run)

    def test_textcontent_constructor(self) -> None:
        from mcp.types import TextContent

        tc = TextContent(type="text", text="hello")
        assert tc.type == "text"
        assert tc.text == "hello"

    def test_calltoolresult_with_structured_content(self) -> None:
        from mcp.types import CallToolResult, TextContent

        result = CallToolResult(
            content=[TextContent(type="text", text='{"success": true}')],
            structuredContent={"success": True},
            isError=False,
            _meta={"serverVersion": "0.1.3"},
        )
        assert result.structuredContent == {"success": True}
        assert result.isError is False

    def test_calltoolresult_meta_alias_serializes(self) -> None:
        from mcp.types import CallToolResult, TextContent

        result = CallToolResult(
            content=[TextContent(type="text", text="{}")],
            _meta={"serverVersion": "0.1.3"},
        )
        dumped = result.model_dump(by_alias=True)
        assert dumped["_meta"] == {"serverVersion": "0.1.3"}


class TestServerInstance:
    def test_server_mcp_instance_loads(self) -> None:
        from gnome_ui_mcp.server import mcp

        assert mcp.name == "gnome-ui-mcp"
