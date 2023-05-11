import styles from "./style.module.css";

export default function Card({ title, price }) {
  return (
    <div className="col-md-3">
      <div className={styles["product"]}>
        <div className={styles["image"]}>
          <img src="http://placehold.it/300x400" alt="" />
        </div>

        <div className={styles["info"]}>
          <h3>{title}</h3>
          <ul className={styles["rating"]}>
            <li>
              <ion-icon name="star"></ion-icon>
            </li>
            <li>
              <ion-icon name="star"></ion-icon>
            </li>
            <li>
              <ion-icon name="star"></ion-icon>
            </li>
            <li>
              <ion-icon name="star"></ion-icon>
            </li>
            <li>
              <ion-icon name="star-half-outline"></ion-icon>
            </li>
          </ul>
          <div className={styles["info-price"]}>
            <span className={styles["price"]}>
              {price}
              <small>₽</small>
            </span>
            <button className={styles["add-to-favourites"]}>
              <ion-icon name="heart-outline"></ion-icon>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
