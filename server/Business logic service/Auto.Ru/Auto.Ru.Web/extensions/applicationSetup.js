const express = require("express");
const cors = require("cors");
const cookieParser = require("cookie-parser");
const { favorites } = require("../models");

// Import local modules
const authMiddleware = require("./auth").authMiddleware;
const filterExceptions = require("./exceptions").filterExceptions;

function setupMiddlewares(app) {
    const cars = require("../routers/carsRouter");
    const favorites = require("../routers/favoritesRouter");

    app.use(
      cors({
        origin: "http://localhost:3000",
        methods: ["GET", "POST", "PUT", "DELETE"],
        allowedHeaders: ["Content-Type", "Authorization"],
        credentials: true,
      })
    );

    app.use(express.json());

    app.use(cookieParser());

    app.use(filterExceptions(authMiddleware));

    app.use("/api/cars", cars);

    app.use("/api/favorites", favorites)

    app.use(function(err, req, res, next){
        console.log(err);
        res.status(500);
        res.send({ message: err.message});
      });
}

module.exports = {setupMiddlewares};