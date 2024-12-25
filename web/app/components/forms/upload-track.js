import Alpine from "alpinejs";

function UploadTrackForm()
{
    return {
        file: undefined,

        errors: {},

        updateFile(event)
        {
            this.file = event.target.files[0];
        },

        async submit() {
            if (!this.file)
            {
                this.errors["file"] = "Please select an mp3 file from your computer to upload";

                return;
            }

            const formData = new FormData();
            formData.append("file", this.file);

            try
            {
                const response = await fetch("/api/tracks", {
                    method: "POST",
                    body: formData,
                });

                if (!response.ok)
                {
                    this.errors.upload = "There was an error trying to upload your track";

                    return;
                }
            }
            catch (error)
            {
                this.errors.upload = "There was an error trying to upload your track";
            }
        },
    };
}

Alpine.data("UploadTrackForm", UploadTrackForm);

export default UploadTrackForm;
