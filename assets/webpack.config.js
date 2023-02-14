const path = require('path');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const RemoveEmptyScriptsPlugin = require('webpack-remove-empty-scripts')

module.exports = {
  entry: {
    main: './src/js/index.js',
    vanilla: './src/js/vanilla_js.js',
    styles: './src/scss/index.scss'
  },
  output: {
    filename: '[name].[contenthash].js',
    publicPath: '/static/dist/',
    path: path.resolve(__dirname, '..','weather_app', 'static', 'dist'),
    clean: true
  },
  module: {
        rules: [{
            test: /\.scss$/,
            use: [
                MiniCssExtractPlugin.loader,
                {
                    loader: 'css-loader'
                },
                {
                    loader: 'sass-loader',
                    options: {
                        sourceMap: true,
                    }
                }
            ]
        }]
    },
  plugins: [
    new WebpackManifestPlugin(),
    new MiniCssExtractPlugin({
            filename: '[name].[contenthash].css'
    }),
    new RemoveEmptyScriptsPlugin()
  ]
};