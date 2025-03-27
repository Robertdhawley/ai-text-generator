{ pkgs }: {
  deps = [
    pkgs.python3
    pkgs.python3Packages.transformers
    pkgs.python3Packages.tensorflow
  ];
}