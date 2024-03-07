module com.example.mymusicplayer {
    requires javafx.controls;
    requires javafx.fxml;

    requires com.dlsc.formsfx;
    requires javafx.media;

    opens com.example.mymusicplayer to javafx.fxml;
    exports com.example.mymusicplayer;
}
