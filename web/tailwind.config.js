/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./app/templates/**/*.html",
        "./app/components/**/*.js",
        "./public/**/*.js",
    ],

    theme: {
        extend: {},
    },

    plugins: [
        require("@tailwindcss/forms"),
        //require("@tailwindcss/typography"),
    ],
};
