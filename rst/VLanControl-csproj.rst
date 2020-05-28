{{example code$(Platform)' == 'Debug$(Platform)' == 'Release|AnyCPU' ">
   <DebugType>pdbonly</DebugType> <Optimize>true</Optimize>
   <OutputPath>binRelease</OutputPath>
   <DefineConstants>TRACE</DefineConstants>
   <ErrorReport>prompt</ErrorReport> <WarningLevel>4</WarningLevel>
   <AllowUnsafeBlocks>false</AllowUnsafeBlocks>
   <RegisterForComInterop>false</RegisterForComInterop>

</PropertyGroup>
   <ItemGroup>
      <Reference Include="System" /> <Reference Include="System.Data" />
      <Reference Include="System.Drawing" /> <Reference
      Include="System.Windows.Forms" /> <Reference Include="System.Xml"
      />

   </ItemGroup> <ItemGroup> <Compile Include="InnerVlcWindow.cs">
   <SubType>UserControl</SubType> </Compile> <Compile
   Include="InnerVlcWindow.Designer.cs">
   <DependentUpon>InnerVlcWindow.cs</DependentUpon> </Compile> <Compile
   Include="IPlayer.cs" /> <Compile Include="NativeLibVlc.cs" />
   <Compile Include="PropertiesAssemblyInfo.cs" /> <Compile
   Include="VlcUserControl.cs"> <SubType>UserControl</SubType>
   </Compile> <Compile Include="VlcUserControl.Designer.cs">
   <DependentUpon>VlcUserControl.cs</DependentUpon> </Compile>
   </ItemGroup> <ItemGroup> <EmbeddedResource
   Include="VlcUserControl.resx"> <SubType>Designer</SubType>
   <DependentUpon>VlcUserControl.cs</DependentUpon> </EmbeddedResource>
   </ItemGroup> <ItemGroup> <None Include="VLanControl.snk" />
   </ItemGroup> <ItemGroup> <Content Include="Test.html" /> </ItemGroup>
   <Import Project="$(MSBuildBinPath)Microsoft.CSharp.targets" /> <!--
   To modify your build process, add your task inside one of the targets
   below and uncomment it. Other similar extension points exist, see
   Microsoft.Common.targets. <Target Name="BeforeBuild"> </Target>
   <Target Name="AfterBuild"> </Target> -->

</Project> </syntaxhighlight></big>
