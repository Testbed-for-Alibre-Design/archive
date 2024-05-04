using Godot;
using ImGuiGodot;
using ImGuiNET;
using System;
using System.Diagnostics;
namespace TestbedImgui;
public partial class Init : Node
{
	private Window _window;
	private static bool fontLoaded = false;
	private ImFontPtr proggy;
	private ColorRect background;
	public override void _EnterTree()
	{
		if (!fontLoaded)
		{
			ImGuiGD.ResetFonts();
			ImGuiGD.AddFont(GD.Load<FontFile>("res://data/Hack-Regular.ttf"), 14);
			ImGuiGD.AddFont(GD.Load<FontFile>("res://data/MPLUS2-Regular.ttf"), 16, merge: true);
			ImGuiGD.AddFontDefault();
			ImGuiGD.RebuildFontAtlas();
			fontLoaded = true;
		}
		var io = ImGui.GetIO();
		io.ConfigFlags |= ImGuiConfigFlags.NavEnableGamepad;
		proggy = io.Fonts.Fonts[1];
		background = GetNode<ColorRect>("/root/Background");
	}
	private static string _text = "";
	private static string _textArea = "";
	public override void _Ready()
	{
		ImGuiLayer.Connect(OnImGuiLayout);
		_window = GetWindow();
	}
	public override void _Process(double delta)
	{
		ImGui.Begin("Alibre Design Tools WIP 1");
		if (ImGui.Button("open"))
		{
			AlibreToImGuiProcessing();
		}
		var size = ImGui.GetWindowSize();
		ImGui.InputTextMultiline("Parameters", ref _textArea, 100, new System.Numerics.Vector2(500,500));
		ImGui.Text(_window.Size.X.ToString());
		ImGui.Text(_window.Size.Y.ToString());
		ImGui.Text(_window.Title.ToString());
		ImGui.Text(size.X.ToString());
		ImGui.Text(size.Y.ToString());
		ImGui.Text(size.ToString());
		ImGui.End();
	}
	private void OnImGuiLayout()
	{
		if (ImGui.Begin("Alibre Design Tools WIP 2"))
		{
			if (ImGui.InputText("Input Field", ref _text, 100))
			{
				GD.Print("text: " + _text);
			}
		}
		ImGui.End();
	}
	public static void AlibreToImGuiProcessing()
    {
        string filePath = @"J:\Testbed-For-Alibre-Design\0-for-github\STAGING\testbed.imgui.alibre\testbed.imgui.alibre\bin\Debug\testbed.imgui.alibre.exe";
		ProcessStartInfo psi = new ProcessStartInfo()
		{
			FileName = filePath,
			CreateNoWindow = true,
			UseShellExecute = false,
			WindowStyle = ProcessWindowStyle.Hidden,
			Arguments = "GetParameterNamesAndValues",
			RedirectStandardOutput = true,
		};
		Process process = new Process();
		process.StartInfo = psi;
		try
		{
			process.Start();
			string output = process.StandardOutput.ReadToEnd();
			process.WaitForExit();
			_textArea = output;
			GD.Print(output);
		}
		catch (Exception ex)
		{
			GD.Print("Error starting external process: " + ex.Message);
		}
	}
}
